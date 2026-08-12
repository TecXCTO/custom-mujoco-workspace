import mujoco
import mujoco.viewer
import time

model = mujoco.MjModel.from_xml_path("../models/simple_pendulum.xml")
data = mujoco.MjData(model)

# Give an initial nudge to the pendulum body
data.qpos[0] = 1.5

print("Launching native simulation renderer loop...")
# Open a responsive interactive GUI window directly via Python bindings
with mujoco.viewer.launch_passive(model, data) as viewer:
    start_time = time.time()
    
    while viewer.is_running() and data.time < 5.0:
        step_start = time.time()

        # Step 1: Advance continuous-time internal physics physics equations
        mujoco.mj_step(model, data)

        # Step 2: Keep interactive window frame refreshed
        viewer.sync()

        # Step 3: Synchronize execution time to maintain real-time visualization pace
        time_elapsed = time.time() - step_start
        if time_elapsed < model.opt.timestep:
            time.sleep(model.opt.timestep - time_elapsed)

print(f"Simulation concluded cleanly at runtime mark: {data.time:.2f} seconds.")
