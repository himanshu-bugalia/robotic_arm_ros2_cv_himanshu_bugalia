from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("robotic_arm_description"),
                "launch","gazebo.launch.py"
            )
        )   
    )

    controllers = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("roboticarm_controller"),
                "launch","controller.launch.py"
            )
        )
    )

    moveit = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("robotic_arm_moveit"),"launch","moveit.launch.py")
        )
    )

    vision = Node(
        package="robotic_arm_perception",
        executable="color_detector",
        name= 'color_dector',
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        # controllers,
        moveit,
        vision
    ])