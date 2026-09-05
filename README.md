<h1 align="center">🤖 ROS2-Based 3-DOF Robotic Arm with Gripper | MoveIt2 + Gazebo Vision-Guided Pick & Place</h1>

<p align="center">
  ROS2 Humble • MoveIt2 • pymoveit2 • Gazebo • TF2 • URDF/Xacro • OpenCV • ros2_control
</p>

<p align="center">
A ROS2-based robotic manipulation system implementing perception, motion planning, control, and simulation using MoveIt2, ros2_control, OpenCV, and Gazebo. A camera detects a target object (via color detection), MoveIt2 plans a grasp trajectory through <code>pymoveit2</code>, and the arm executes a full pick-and-place sequence on a simulated robot in Gazebo — a complete perception-to-action digital twin pipeline.
</p>

---

## 🎥 Project Demos

### 🦾 Arm Motion Planning + Gazebo Execution

https://github.com/user-attachments/assets/fcd272e6-22be-42c3-95cd-de1ab4f5a574

🚀 Demonstrates a complete planning-to-execution pipeline used in real-world robotic systems

### 🤏 Gripper Motion Demo

https://github.com/user-attachments/assets/66b2b837-64e9-4d77-9a32-0c9a154dee75

✔ Demonstrates synchronized motion execution between MoveIt (planning) and Gazebo (simulation)

### 🎯 Full Vision-Guided Pick & Place Demo

https://github.com/user-attachments/assets/1413e955-63a3-46aa-a167-31a3e94904d2

🧠 End-to-end pipeline: OpenCV/color-based object detection → pymoveit2 grasp planning → synchronized execution in Gazebo and RViz

---

## ✨ Features

- 🎨 **Object Detection**: OpenCV-based color detection (Red, Green, Blue)
- 🦾 **Motion Planning**: Collision-aware trajectory planning via MoveIt2
- 🎯 **Autonomous Pick & Place**: Full detect → plan → grasp → place pipeline via `final_build`
- 🐍 **Python-level Control**: High-level trajectory/grasp control using `pymoveit2`
- 🌐 **TF2 Frame Validation**: Verified transforms between camera, arm, and object frames
- 📊 **RViz + Gazebo Visualization**: Synchronized planning display and physics simulation
- 🔧 **ros2_control Integration**: Joint trajectory controllers for arm and gripper

---

## 📋 Table of Contents

1. [💻 Installation](#-installation)
2. [🏗️ Build the Workspace](#-build-the-workspace)
3. [🎮 Running the Project](#-running-the-project)
4. [📂 Repository Structure](#-repository-structure)
5. [🚀 How It Works](#-how-it-works)
6. [💡 Customization Guide](#-customization-guide)
7. [⚠️ Troubleshooting](#️-troubleshooting)
8. [📚 References](#-references)

---

# 💻 Installation

## Prerequisites

- **Ubuntu 22.04 LTS** (ROS2 Humble)
- **8GB+ RAM** recommended for Gazebo simulation
- **10GB+ free disk space**

## Step 1: Install ROS2 Humble

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
sudo apt install ros-humble-desktop-full -y

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## Step 2: Install MoveIt2, Gazebo, and Vision Dependencies

```bash
sudo apt install -y \
  ros-humble-moveit \
  ros-humble-moveit-ros-move-group \
  ros-humble-moveit-ros-planning-interface \
  ros-humble-moveit-visual-tools \
  ros-humble-ros2-control \
  ros-humble-ros2-controllers \
  ros-humble-gazebo-ros2-control \
  ros-humble-ros-gz \
  ros-humble-cv-bridge \
  ros-humble-image-transport \
  ros-humble-rqt-graph \
  ros-humble-rqt-image-view

pip3 install --no-cache-dir opencv-python numpy transforms3d
```

## Step 3: Development Tools

```bash
sudo apt install python3-rosdep python3-colcon-common-extensions python3-pip -y
sudo rosdep init
rosdep update
```

---

# 🏗️ Build the Workspace

```bash
mkdir -p ~/robotic_arm_ws/src
cd ~/robotic_arm_ws/src
git clone https://github.com/himanshu-bugalia/robotic_arm_ros2_cv_himanshu_bugalia.git .

cd ~/robotic_arm_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash

echo "source ~/robotic_arm_ws/install/setup.bash" >> ~/.bashrc
```

**Verify installation:**

```bash
ros2 pkg list | grep robotic_arm
# Expected output:
# robotic_arm_description
# robotic_arm_moveit
# robotic_arm_perception
# roboticarm_controller
```

---

# 🎮 Running the Project

Open separate terminals for each stage, sourcing the workspace in each (`source ~/robotic_arm_ws/install/setup.bash`).

### Terminal 1 — Gazebo (pick-and-place world)
```bash
ros2 launch robotic_arm_description gazebo.launch.py
```

### Terminal 2 — Controllers
```bash
ros2 launch roboticarm_controller controller.launch.py
```

### Terminal 3 — MoveIt2
```bash
ros2 launch robotic_arm_moveit moveit.launch.py
```

### Terminal 4 — Full Vision-Guided Pipeline
```bash
ros2 launch final_build pick_and_place.launch.py
```

This brings up perception (`robotic_arm_perception`), planning (`pymoveit2` + MoveIt2), and execution (Gazebo + controllers) together, and runs a full detect → plan → grasp → place cycle.

## 🔍 Useful Monitoring Commands

```bash
ros2 node list
ros2 topic list
ros2 topic echo /joint_states
ros2 run rqt_image_view rqt_image_view     # view camera feed
ros2 run rqt_graph rqt_graph                # visualize computation graph
```

---

# 📂 Repository Structure

```bash
robotic_arm_ros2_cv_himanshu_bugalia/
├── robotic_arm_description/     # URDF/Xacro, meshes, worlds, Gazebo models
│   ├── assets/
│   ├── models/
│   ├── worlds/
│   ├── launch/
│   └── urdf/
│
├── robotic_arm_moveit/          # MoveIt2 motion planning configuration
│   ├── config/
│   └── launch/
│
├── robotic_arm_perception/      # OpenCV-based /color detection node
│   ├── robotic_arm_perception/
│   └── test/
│
├── roboticarm_controller/       # ROS2 controllers, trajectory execution, gripper control
│   ├── config/
│   └── launch/
│
├── pymoveit2/                   # Python MoveIt2 interface (grasp planning/execution)
│
├── final_build/                 # Top-level pick-and-place launch pipeline
│   └── launch/
│
├── README.md
└── .gitignore
```

## 🧩 Package Overview

| Package | Description |
|---|---|
| **robotic_arm_description** | URDF/Xacro robot model, meshes, RViz config, Gazebo worlds & models |
| **robotic_arm_moveit** | MoveIt2 motion planning configuration and launch |
| **robotic_arm_perception** | Camera-based object detection (  marker / color-based) |
| **roboticarm_controller** | ROS2 controllers, trajectory execution, gripper control |
| **pymoveit2** | Python interface to MoveIt2 for programmatic grasp planning |
| **final_build** | Integrates perception + planning + control into one pick-and-place launch |

# 🚀 How It Works

## System Architecture

```
Camera Feed → Color<img width="1907" height="1028" alt="Screenshot 2026-09-05 100734" src="https://github.com/user-attachments/assets/79e6bed8-3ce7-48e4-9be2-5344c4d469b2" />
 Detection → Object Pose Estimation
                                            ↓
                                  pymoveit2 Grasp Planning
                                            ↓
                                MoveIt2 Trajectory Planning
                                            ↓
                              ros2_control Trajectory Execution
                                            ↓
                        Gazebo Simulation ←→ RViz Visualization
```

## Workflow

1. Model robotic arm in **URDF/Xacro**
2. Validate DOFs in **RViz2**
3. Verify frame hierarchy using **TF2**
4. Configure **MoveIt2** motion planning
5. Detect target object pose via **OpenCV** in `robotic_arm_perception`
6. Plan and execute grasp trajectory via **pymoveit2**
7. Execute trajectories in **Gazebo** with synchronized gripper control
8. Integrate all stages into a single pipeline in **final_build**

---

# 💡 Customization Guide

### Adjust color detection thresholds
Edit `robotic_arm_perception/robotic_arm_perception/color_detector.py`:
```python
red_lower = (0, 120, 70)
red_upper = (10, 255, 255)
```

### Change pick/place target poses
Edit the pose targets inside `final_build/launch/pick_and_place.launch.py` or the `pymoveit2` example script driving the sequence.

### Tune motion planning
Edit `robotic_arm_moveit` config (planning time, velocity/acceleration scaling) for smoother or faster execution.

---

# ⚠️ Troubleshooting

### 🔴 Gazebo won't start / segfaults
```bash
killall gzserver gzclient
rm -rf ~/.gazebo/
export LIBGL_ALWAYS_SOFTWARE=1   # fallback to software rendering
```

### 🔴 RViz shows black screen
```bash
rm -rf ~/.rviz2/
echo $DISPLAY
```

### 🔴 MoveIt planning fails ("no valid plan found")
```bash
ros2 control list_controllers
```
Check for collisions in the scene and confirm the robot's current state in RViz matches Gazebo.

### 🔴 No camera feed on `/camera/image_raw`
```bash
ros2 topic list | grep camera
```
Confirm the camera plugin loaded in the Gazebo world, then restart the launch file.

### 🔴 Color detection not working
- Check HSV thresholds in `color_detector.py`
- Verify lighting/marker visibility in Gazebo
- Inspect the feed directly: `ros2 run rqt_image_view rqt_image_view`

---

# 📚 References

- 🌐 [ROS2 Humble Docs](https://docs.ros.org/en/humble/)
- 🌐 [MoveIt2](https://moveit.picknik.ai/humble/index.html)
- 🌐 [pymoveit2](https://github.com/AndrejOrsula/pymoveit2)
- 🌐 [Gazebo](https://gazebosim.org/)
- 📖 [ros2_control](https://control.ros.org/)

---

## 👨‍💻 Author

**Himanshu Bugalia**
Mechanical Engineering | SGSITS Indore
Robotics • ROS2 • Computer Vision • Digital Twin
