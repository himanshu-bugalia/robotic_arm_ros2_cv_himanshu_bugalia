<h1 align="center">🤖 Smart 4-DOF Robotic Arm ROS2 Pipeline</h1>

<p align="center">
  ROS2 Humble • MoveIt2 • Gazebo • TF2 • URDF/Xacro • OpenCV • ros2_control
</p>

<p align="center">
  A simulation-first robotic arm project featuring motion planning, TF tree validation, gripper actuation, and future vision-based pick & place integration.
</p>

---

## 🎥 Project Demos

### 🦾 Arm Motion Planning + Gazebo Execution



https://github.com/user-attachments/assets/8cba3138-fb6c-40a2-a577-498ec98ff462








### 🤏 Gripper Motion Demo





https://github.com/user-attachments/assets/19e05b8b-1f19-4ccd-9fd3-48055bf2a728





---

## 📸 Visual Outputs

### 🧩 URDF Model with Joint Sliders GUI
<p align="center">
  <img src="robotic_arm_description/assets/urdf_joint_gui.png" width="900"/>
</p>

### 🌐 TF2 Frame Tree Graph
<p align="center">
  <img src="robotic_arm_description/assets/tf_tree_graph.png" width="900"/>
</p>

### 📍 TF Runtime Visualization
<p align="center">
  <img src="robotic_arm_description/assets/tf_tree_screenshot.png" width="900"/>
</p>

---

## ✨ Key Features
- ✅ 4-DOF robotic arm URDF/Xacro modeling
- ✅ RViz2 joint GUI verification
- ✅ MoveIt2 inverse kinematics + planning
- ✅ Interactive marker based end-effector control
- ✅ Gazebo synchronized execution
- ✅ Gripper open-close motion
- ✅ TF2 frame graph validation
- ✅ ros2_control integration
- 🔄 OpenCV based vision pipeline *(in progress)*
- 🔄 Real hardware synchronization *(future scope)*

---

## 🛠️ Tech Stack
| Category | Tools |
|---|---|
| Middleware | ROS2 Humble |
| Planning | MoveIt2 |
| Simulation | Gazebo |
| Visualization | RViz2 |
| Frames | TF2 |
| Robot Model | URDF / Xacro |
| Vision | OpenCV |
| Control | ros2_control |
| Languages | Python, C++ |
| OS | Ubuntu 22.04 |

---

## 📂 Repository Structure
```bash
robotic_arm_ros2_cv_himanshu_bugalia/
├── robotic_arm_description/
│   ├── assets/
│   ├── config/
│   ├── launch/
│   ├── meshes/
│   ├── rviz/
│   ├── urdf/
│   └── worlds/
│
├── robotic_arm_moveit/
│   ├── config/
│   ├── launch/
│   ├── srdf/
│   └── rviz/
│
├── roboticarm_controller/
│   ├── src/
│   ├── include/
│   ├── launch/
│   └── config/
│
├── README.md
└── .gitignore
```
## 🧠 Package Responsibilities
- **robotic_arm_description** → URDF/Xacro, meshes, RViz, Gazebo world
- **robotic_arm_moveit** → MoveIt2 motion planning and execution pipeline
- **roboticarm_controller** → ROS2 controllers, trajectory execution, gripper control
---

## ⚙️ Workflow
1. Model robotic arm in **URDF/Xacro**
2. Validate DOFs in **RViz2**
3. Verify frame hierarchy using **TF2**
4. Configure **MoveIt2 motion planning**
5. Execute trajectories in **Gazebo**
6. Integrate gripper control
7. Extend toward **OpenCV based object detection**
8. Future digital twin + hardware sync

---

## 🚀 Future Scope
- 🎯 Color-based object detection
- 📦 Vision-guided pick & place
- 🤖 Physical robotic arm integration
- 🌐 Digital twin synchronization
- 📡 micro-ROS serial communication
- 🧠 AI-based object classification

---

## 👨‍💻 Author
**Himanshu Bugalia**  
Mechanical Engineering | SGSITS Indore  
Robotics • ROS2 • Computer Vision • Digital Twin
