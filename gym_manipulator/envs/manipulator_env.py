import os
import gymnasium as gym
from gymnasium import spaces
import mujoco
import numpy as np

class ManipulatorEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 50}

    def __init__(self, render_mode=None):
        super().__init__()
        
        # Load the MJCF Model
        xml_path = os.path.join(os.path.dirname(__file__), '../../assets/manipulator/arm_scene.xml')
        self.model = mujoco.MjModel.from_xml_path(xml_path)
        self.data = mujoco.MjData(self.model)

        self.render_mode = render_mode
        self.viewer = None

        # Action space: 2 Continuous motor torques inside range [-1, 1]
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2,), dtype=np.float32)

        # Observation space: qpos(2), qvel(2), target_pos(3), ee_pos(3) = 10 structural features
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(10,), dtype=np.float32)

    def _get_obs(self):
        # Extract robot state configurations
        qpos = self.data.qpos.copy()
        qvel = self.data.qvel.copy()
        
        # Extract 3D Cartensian coordinates from simulation sites
        ee_pos = self.data.site('ee_site').xpos.copy()
        target_pos = self.data.body('target').xpos.copy()
        
        return np.concatenate([qpos, qvel, target_pos, ee_pos], dtype=np.float32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        # Reset physics variables back to baseline layout
        mujoco.mj_resetData(self.model, self.data)

        # Randomize target position smoothly at every new episode start
        target_id = self.model.body('target').id
        self.model.body_pos[target_id] = np.array([
            self.np_random.uniform(0.2, 0.5),
            0.0,
            self.np_random.uniform(0.2, 0.6)
        ])

        # Randomize initial robot joint positions slightly to prevent overfitting
        self.data.qpos[0] = self.np_random.uniform(-0.5, 0.5)
        self.data.qpos[1] = self.np_random.uniform(-0.5, 0.5)
        mujoco.mj_forward(self.model, self.data)

        if self.render_mode == "human":
            self.render()

        return self._get_obs(), {}

    def step(self, action):
        # 1. Inject agent actions into motor controls
        self.data.ctrl[:] = action
        
        # 2. Advance physics simulation frames
        # Run 10 sub-steps to match rendering frame rate constraints cleanly
        for _ in range(10):
            mujoco.mj_step(self.model, self.data)

        obs = self._get_obs()

        # 3. Calculate Reward (Negative Euclidean distance between End Effector and Target)
        ee_pos = self.data.site('ee_site').xpos
        target_pos = self.data.body('target').xpos
        distance = np.linalg.norm(ee_pos - target_pos)
        
        reward = -distance  # Shorter distance yields higher rewards
        reward -= 0.1 * np.sum(np.square(action))  # Penalize excessive, jerky control efforts

        # 4. Define termination/truncation parameters
        terminated = False
        truncated = self.data.time > 4.0  # Cap every training episode at 4 simulated seconds

        if self.render_mode == "human":
            self.render()

        return obs, reward, terminated, truncated, {}

    def render(self):
        if self.render_mode == "human" and self.viewer is None:
            import mujoco.viewer
            self.viewer = mujoco.viewer.launch_passive(self.model, self.data)
        
        if self.viewer is not None:
            self.viewer.sync()

    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None
          
