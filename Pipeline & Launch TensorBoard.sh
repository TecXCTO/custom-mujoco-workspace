# Part 3: Run the Pipeline & Launch TensorBoardExecute these commands in your workspace to run the script and launch your metrics dashboard.

# 1. Run the training script to begin saving metrics
python scripts/train.py

# 2. Open a separate terminal and launch TensorBoard to track curves live
tensorboard --logdir ./tensorboard_logs/

# Once executed, open your browser and navigate to http://localhost:6006 to monitor value loss drops and mean episode reward trends.
# 3. Commit the 3-DOF and TensorBoard feature upgrades to GitHub
git add assets/manipulator/arm_scene.xml gym_manipulator/envs/manipulator_env.py scripts/train.py
git commit -m "Upgrade model to 3-DOF spatial arm and integrate live TensorBoard logging metric tracking"
git push origin main
