import mujoco
import mujoco.viewer
import numpy as np
import time

model = mujoco.MjModel.from_xml_path("../models/simple_pendulum.xml")
data = mujoco.MjData(model)

# Define target setpoint reference and feedback variables
TARGET_ANGLE = 0.0  # Force pendulum to stand straight up vertically
kp = 12.0          # Proportional feedback coefficient
kd = 3.5           # Derivative damping coefficient
ki = 0.5           # Integral error handling factor

integral_error = 0.0
data.qpos[0] = -2.5 # Start upside down from a steep angle

print("Initializing tracking controller loop...")
with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running() and data.time < 8.0:
        # 1. Capture current errors from physical tracking states
        current_position = data.qpos[0]
        current_velocity = data.qvel[0]
        
        position_error = TARGET_ANGLE - current_position
        integral_error += position_error * model.opt.timestep
        
        # 2. Compute PID outputs using classic feedback equations
        control_torque = (kp * position_error) + (ki * integral_error) - (kd * current_velocity)
        
        # 3. Restrict outputs within mechanical safety limits defined in MJCF
        control_torque = np.clip(control_torque, model.actuator_ctrlrange[0, 0], model.actuator_ctrlrange[0, 1])
        
        # 4. Bind the computation directly into the motor input register
        data.ctrl[0] = control_torque

        # 5. Process tracking updates inside the solver engine
        mujoco.mj_step(model, data)
        viewer.sync()
        
        time.sleep(model.opt.timestep)
      
