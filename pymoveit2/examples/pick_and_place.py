#!/usr/bin/env python3
from threading import Thread
import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from std_msgs.msg import String

from pymoveit2 import MoveIt2, GripperInterface

import math


class PickAndPlace(Node):
    def __init__(self):
        super().__init__("pick_and_place")

        self.declare_parameter("target_color", "R")
        self.target_color = self.get_parameter("target_color").value.upper()

        self.declare_parameter("approach_offset", 0.6)
        self.approach_offset = float(self.get_parameter("approach_offset").value)

        self.already_moved = False
        self.target_coords = None

        self.callback_group = ReentrantCallbackGroup()

        # Arm MoveIt2 interface — configured for robotic_arm (3-DOF)
        self.moveit2 = MoveIt2(
            node=self,
            joint_names=["joint_1", "joint_2", "joint_3"],
            base_link_name="base_link",
            end_effector_name="claw_support",
            group_name="arm",
            callback_group=self.callback_group,
        )

        self.moveit2.max_velocity = 0.1
        self.moveit2.max_acceleration = 0.1

        # Gripper interface — joint_4 actuated, joint_5 mimics joint_4
        self.gripper = GripperInterface(
            node=self,
            gripper_joint_names=["joint_4"],
            open_gripper_joint_positions=[-0.8],     # CONFIRM actual open value
            closed_gripper_joint_positions=[0.0],    # CONFIRM actual closed value
            gripper_group_name="gripper",
            callback_group=self.callback_group,
            gripper_command_action_name="gripper_controller/gripper_cmd",  # CONFIRM actual action name
        )

        self.sub = self.create_subscription(
            String, "/color_coordinates", self.coords_callback, 10
        )
        self.get_logger().info(f"Waiting for {self.target_color} from /color_coordinates...")

        # 3-DOF joint configurations — VALUES ARE PLACEHOLDERS, verify safe/reachable
        self.start_joints = [0.0, 0.0, 0.0]
        self.home_joints  = [0.0, math.radians(-30.0), math.radians(30.0)]
        self.drop_joints  = [math.radians(90.0), math.radians(-20.0), math.radians(-27.0)]

        self.moveit2.move_to_configuration(self.start_joints)
        self.moveit2.wait_until_executed()

    def coords_callback(self, msg):
        if self.already_moved:
            return
        try:
            color_id, x, y, z = msg.data.split(",")
            color_id = color_id.strip().upper()

            if color_id == self.target_color:
                self.target_coords = [float(x), float(y), float(z)]
                self.get_logger().info(f"Target {self.target_color} locked at: {self.target_coords}")
                self.already_moved = True

                pick_position = [self.target_coords[0], self.target_coords[1], self.target_coords[2] - 0.5]
                quat_xyzw = [1.0, 0.0, 0.0, 0.0]

                self.get_logger().info("moving to home pose")

                self.moveit2.move_to_configuration(self.home_joints)
                self.moveit2.wait_until_executed()

                self.get_logger().info("moving to pick up pose")

                self.moveit2.move_to_pose(position=pick_position, quat_xyzw=quat_xyzw)
                self.moveit2.wait_until_executed()

                self.get_logger().info("gripper is opening")

                self.gripper.open()
                self.gripper.wait_until_executed()

                self.get_logger().info("approaching to box")

                approach_position = [pick_position[0], pick_position[1], pick_position[2] - self.approach_offset]
                # approach_position = [pick_position[0], pick_position[1], pick_position[2]]
                self.moveit2.move_to_pose(position=approach_position, quat_xyzw=quat_xyzw, cartesian=True)
                self.moveit2.wait_until_executed()

                self.get_logger().info("gripper is closeing")

                self.gripper.close()
                self.gripper.wait_until_executed()

                self.get_logger().info("moving to home pose")

                self.moveit2.move_to_configuration(self.home_joints)
                self.moveit2.wait_until_executed()

                self.get_logger().info("moving to drop pose")

                self.moveit2.move_to_configuration(self.drop_joints)
                self.moveit2.wait_until_executed()

                self.get_logger().info("gripper is opening")

                self.gripper.open()
                self.gripper.wait_until_executed()

                self.get_logger().info("gripper is closeing")

                self.gripper.close()
                self.gripper.wait_until_executed()

                self.get_logger().info("moving to start pose")

                self.moveit2.move_to_configuration(self.start_joints)
                self.moveit2.wait_until_executed()

                self.get_logger().info("Pick-and-place sequence complete.")
                rclpy.shutdown()

        except Exception as e:
            self.get_logger().error(f"Error parsing /color_coordinates: {e}")


def main():
    rclpy.init()
    node = PickAndPlace()
    executor = rclpy.executors.MultiThreadedExecutor(2)
    executor.add_node(node)
    executor_thread = Thread(target=executor.spin, daemon=True)
    executor_thread.start()
    try:
        executor_thread.join()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()