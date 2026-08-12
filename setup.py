# This allows you to install your custom environment locally using pip install -e .
from setuptools import setup, find_packages

setup(
    name="gym_manipulator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "mujoco>=3.0.0",
        "gymnasium>=0.29.0",
        "stable-baselines3>=2.0.0",
        "numpy<2.0.0",
    ],
)
