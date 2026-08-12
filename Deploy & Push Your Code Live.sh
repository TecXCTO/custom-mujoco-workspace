# 1. Execute your training script to watch the arm actively learn to steer away from the obstacle
python scripts/train.py

# 2. Stage and commit your final updates to GitHub
git add gym_manipulator/envs/manipulator_env.py
git commit -m "Implement safe RL with terminal collision constraints and shaped proximity penalties"
git push origin main
