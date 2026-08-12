import gymnasium as gym
from stable_baselines3 import PPO
import gym_manipulator  # Triggers explicit gymnasium workspace mapping initialization

def main():
    print("Initializing Custom MuJoCo Arm Environment via Gymnasium...")
    # Initialize parallel vector environments for training speed optimization
    env = gym.make("GymManipulator-v0")

    print("Building PPO Actor-Critic Neural Network Architecture...")
    model = PPO(
        "MlpPolicy", 
        env, 
        verbose=1, 
        learning_rate=3e-4,
        tensorboard_log="./tensorboard_logs/"
    )

    print("Starting Training Loop Pipeline (100,000 steps)...")
    model.learn(total_timesteps=100000)

    # Save policy weight vectors cleanly upon optimization completion
    model.save("ppo_planar_manipulator")
    print("Training finished! Saved model checkpoints to disk.")

    # Run evaluation live tracking showcase
    eval_env = gym.make("GymManipulator-v0", render_mode="human")
    obs, _ = eval_env.reset()
    
    print("Launching Trained Model Evaluation Showcase Window Loop...")
    for _ in range(1000):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, _ = eval_env.step(action)
        if terminated or truncated:
            obs, _ = eval_env.reset()
            
    eval_env.close()

if __name__ == "__main__":
    main()
