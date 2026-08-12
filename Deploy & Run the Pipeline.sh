# Execute these steps in your terminal to install your package locally, start training your RL model, and back up the entire pipeline to GitHub.
# 1. Install your project locally in editable developer mode
pip install -e .

# 2. Run the pipeline script to train the model and watch the arm learn live
python scripts/train.py

# 3. Save files and commit changes to your Github Repository
git add .
git commit -m "Complete robotic manipulator Gymnasium wrapper with PPO training baseline script"
git push origin main
