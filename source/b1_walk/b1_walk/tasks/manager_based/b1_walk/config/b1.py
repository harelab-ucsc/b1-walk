"""Configuration for the B1 dog.

The following configurations are available:

* :obj:`UNITREE_B1_CFG`: Unitree B1 robot with DC motor model for the legs. Adapted from the A1 CFG.
TODO: match the DC motor actuator to the real specified values from Unitree

Reference:
    - https://github.com/unitreerobotics/unitree_ros
    - /pvc/isaac-sim/IsaacLab/scripts/lemon/main.py
"""

import isaaclab.sim as sim_utils

# from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from pathlib import Path

# Path to current config's directory (.../b1_walk/config)
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / ".." / "models"  # .../b1_walk/models
B1_USD = MODEL_DIR / "b1.usd"  # .../b1_walk/models/b1.usd

##
# Configuration
##

B1_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(B1_USD),
        activate_contact_sensors=True,  # FROM A1 CFG
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
            rigid_body_enabled=True,
            enable_gyroscopic_forces=True,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
        # visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.00, 0.01, 0.01))
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.52),
        joint_pos={
            ".*L_hip_joint": 0.1,
            ".*R_hip_joint": -0.1,
            "F[L,R]_thigh_joint": 0.8,
            "R[L,R]_thigh_joint": 1.0,
            ".*_calf_joint": -1.5,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    # actuators={
    #     "base_legs": DCMotorCfg(
    #         joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
    #         effort_limit= 1000, # 33.5
    #         saturation_effort=1000, # 33.5
    #         velocity_limit=21.0,
    #         stiffness=240, # 25.0
    #         damping=10, # 0.5
    #         friction=0.0,
    #     ),
    # },
    actuators={
        "base_legs": ImplicitActuatorCfg(
            joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
            effort_limit_sim=20000.0,
            velocity_limit_sim=100.0,
            stiffness=250.0,
            damping=1.0,
        ),
    },
)

"""
Note: Check specifications from: https://www.trossenrobotics.com/a1-quadruped#specifications
"""
