from gymnasium.envs.registration import register

register(
    id="GymManipulator-v0",
    entry_point="gym_manipulator.envs:ManipulatorEnv",
    max_episode_steps=200,
)
