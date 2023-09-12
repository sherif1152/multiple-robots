# Multiple Robots Project

Welcome to the Multiple Robots project! 

## Table of Contents

- [Robots](#robots)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)


## Robots

 - Robot 1
 - Robot 2
 - Robot 3

used two wheel and Lidar (Light Detection and Ranging )

## Description 
This Autonomous mobile robot with diff drive ,I built it by  `URDF`, build map and implementation in gazebo .

Used `gmapping pkg` provides laser-based SLAM (Simultaneous Localization and Mapping) to create a 2D occupancy grid map .

Then Used `AMCL` to localization robot moving in the map.

I used Navigation stack its used to enable robots to autonomously navigate and move in their environments while avoiding obstacles and reaching target locations.
 i used using the `move_base package` ,and A* algorithm 


## Installation

To use these robots, follow these installation steps:

1. Creating a workspace:
```
$ mkdir -p ~/multi_robot_ws/src
$ cd ~/catkin_ws/src 
```

2. Clone this repository to your local machine:

```bash
   git clone https://github.com/sherif1152/multiple-robots.git
```
3. 
```
$ cd ..
$ catkin_make
```

## Usage
 1. Run robots in gazebo :
  ```bash
  roslaunch description_pkg robots.launch 
```
 2. Run Nav in RVIZ
 ```
  roslaunch navigtion_pkg multi_navigation.launch 
```




