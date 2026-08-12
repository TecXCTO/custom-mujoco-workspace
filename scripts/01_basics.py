import mujoco
import numpy as np

# Load structural definitions into memory
model = mujoco.MjModel.from_xml_path("../models/simple_pendulum.xml")
data = mujoco.MjData(model)

print("=== MUJOCO STRUCTURAL META DATA ===")
print(f"Number of Generalized Coordinates (qpos): {model.nq}")
print(f"Number of Degrees of Freedom (qvel):      {model.nv}")
print(f"Number of Input Actuators (ctrl):         {model.nu}")

# Manipulate initial state variables directly
data.qpos[0] = np.pi / 4  # Tilt joint angle by 45 degrees
mujoco.mj_forward(model, data) # Evaluate positions and kinematics

print("\n=== SYSTEM STATE CALCULATIONS ===")
print(f"Initial Joint Angle Position: {data.qpos[0]:.4f} rad")
print(f"Global Position of the Tip:   {data.xpos[model.body('tip').id]}")
