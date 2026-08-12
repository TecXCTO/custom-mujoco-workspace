# Custom MuJoCo Python Workspace
Step-by-step robotics simulator ranging from structural MJCF files to real-time closed-loop controllers.

```

```

```
custom-mujoco-workspace/
├── assets/
│   └── manipulator/
│       └── arm_scene.xml         <-- MJCF Robot & Environment Blueprint
├── gym_manipulator/
│   ├── __init__.py               <-- Gymnasium Environment Registration
│   └── envs/
│       ├── __init__.py
│       └── manipulator_env.py    <-- Core Gymnasium/MuJoCo Wrapper Class
├── scripts/
│   └── train.py                  <-- Stable-Baselines3 Reinforcement Learning Training
├── README.md
└── setup.py                      <-- Local pip installation configuration
```
