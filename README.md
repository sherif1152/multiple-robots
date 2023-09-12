# Multiple Robots Project

Welcome to the Multiple Robots project! 

## Table of Contents

- [Robots](#robots)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)


## Robots
This project involves the use of three robots:
 - Robot 1
 - Robot 2
 - Robot 3

Each of these robots is equipped with a two-wheel drive system and Lidar (Light Detection and Ranging) for sensing.

## Description 
These autonomous mobile robots are built using the URDF (Unified Robot Description Format) and are designed for mapping and navigation in a simulated environment using Gazebo. Here are the key components and functionalities:

- *Mapping*: The project utilizes the `gmapping` package to perform laser-based SLAM (Simultaneous Localization and Mapping), creating a 2D occupancy grid map.

- *Localization*: The robots are localized within the map using the `AMCL` (Adaptive Monte Carlo Localization) algorithm.

- *Navigation*: To enable autonomous navigation, the project employs the Navigation stack, allowing the robots to move autonomously in their environments while avoiding obstacles and reaching target locations. This navigation stack utilizes the `move_base` package and the A* algorithm for path planning. 


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
3. Build the workspace:
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




