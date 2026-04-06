# 🦾 Robotic Arm with ROS2 & Computer Vision
![Robot Simulation Preview](./robotic_arm_description/robot_preview.png)

This project focuses on the design, simulation, and autonomous control of a robotic arm using **ROS2 Humble** and **Computer Vision**. It includes custom URDF descriptions for simulation and a dedicated vision pipeline for object detection.

## 📂 Repository Structure

*   **`robotic_arm_description/`**: Contains the robot's physical model (URDF/Xacro) and 3D meshes (STL).
*   **`robotic_arm_vision/`**: (In Development) ROS2 nodes for OpenCV/YOLO-based vision processing.
*   **`robotic_arm_bringup/`**: (Coming Soon) Centralized launch files to start simulation and vision nodes.

## 🛠️ Requirements

- **OS:** Ubuntu 22.04
- **ROS2 Version:** Humble Hawksbill
- **Libraries:** OpenCV, `cv_bridge`, `sensor_msgs`

## 🚀 Getting Started

### 1. Installation
Clone this repository into your ROS2 workspace `src` folder:
```bash
cd ~/robotic_arm_ws/src
git clone https://github.com
