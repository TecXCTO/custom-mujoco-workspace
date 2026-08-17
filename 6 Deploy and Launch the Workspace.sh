# Run these commands in your workspace terminal to execute your code, monitor metrics via TensorBoard, and push your completed files to GitHub.

# 1. Run your updated training pipeline script
python scripts/train.py

# 2. Monitor execution metrics live via TensorBoard
tensorboard --logdir ./tensorboard_logs/

# 3. Stage and commit your final feature upgrades to GitHub
git add assets/manipulator/arm_scene.xml gym_manipulator/envs/manipulator_env.py scripts/train.py
git commit -m "Upgrade arm architecture with position actuators, 2-finger gripper bodies, and picking rewards"
git push origin main
