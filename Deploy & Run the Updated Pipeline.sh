# Deploy & Run the Updated Pipeline
# Execute these commands in your terminal to save your updates and run the new training pipeline.

# 1. Run the training script to watch the robot learn to navigate around the obstacle
python scripts/train.py

# 2. Save your updates to GitHub
git add assets/manipulator/arm_scene.xml gym_manipulator/envs/manipulator_env.py
git commit -m "Add workspace obstacle avoidance mechanics and integrated camera sensor feed arrays"
git push origin main
