import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.substitutions import Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

from launch.actions import ExecuteProcess

def generate_launch_description():
    robotic_arm_description_dir = get_package_share_directory("robotic_arm_description")

    model_arg = DeclareLaunchArgument(name="model", default_value=os.path.join(
                                        robotic_arm_description_dir, "urdf", "robotic_arm.urdf.xacro"
                                        ),
                                      description="Absolute path to robot urdf file")

    
    gazebo_resource_path = SetEnvironmentVariable(
        name="GZ_SIM_RESOURCE_PATH",
        value=":".join([
            str(Path(robotic_arm_description_dir).parent.resolve()),  # for model://robotic_arm_description/meshes/...
            os.path.join(robotic_arm_description_dir, "models"),       # for model://aruco_box_0
        ])
    )

    gz_plugin_path = SetEnvironmentVariable(
        name="GZ_SIM_SYSTEM_PLUGIN_PATH",
        value="/opt/ros/humble/lib"
    )

    ros_distro = os.environ["ROS_DISTRO"]
    is_ignition = "True" if ros_distro == "humble" else "False"

    robot_description = ParameterValue(Command([
        "xacro ",
        LaunchConfiguration("model"),
        " is_ignition:=",
        is_ignition
        ]),
        value_type=str)


    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description,
                     "use_sim_time": True}]
    )

    robotic_arm_world = os.path.join(robotic_arm_description_dir, "worlds", "pick_place_world.sdf")

    gazebo_server = ExecuteProcess(
        cmd=["ign", "gazebo", "-s", "-r", "-v", "4", robotic_arm_world],
        output="screen"
    )

    gazebo_gui = ExecuteProcess(
        cmd=["ign", "gazebo", "-g", "-v", "4"],
        output="screen"
    )

    gz_spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=["-topic", "robot_description",
                   "-name", "roboticarm"],
    )

    gz_ros2_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
            "/image_raw@sensor_msgs/msg/Image[gz.msgs.Image",
            "/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo",
        ],
        output="screen",
    )
    return LaunchDescription([
        model_arg,
        gazebo_resource_path,
        gz_plugin_path,
        robot_state_publisher_node,
        gazebo_server,
        gazebo_gui,
        gz_spawn_entity,
        gz_ros2_bridge,
    ])