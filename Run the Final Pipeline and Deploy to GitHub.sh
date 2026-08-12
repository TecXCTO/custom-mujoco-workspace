# 1. Run the updated training script
python scripts/train.py

# 2. Stage and commit all codebase updates
git add gym_manipulator/envs/manipulator_env.py scripts/train.py
git commit -m "Complete course project: Added vision-optimized PPO hyperparameters and a moving trajectory target"

# 3. Push your entire production code live to GitHub
git push origin main
