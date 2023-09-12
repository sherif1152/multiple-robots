#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion

def move_robot(x, y, angle, robot_name):
    rospy.init_node(f'move_robot_node_{robot_name}', anonymous=True)
    client = actionlib.SimpleActionClient(f'{robot_name}/move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose = Pose(Point(x, y, 0.0), Quaternion(0.0, 0.0, angle, 1.0))

    client.send_goal(goal)
    client.wait_for_result()

if __name__ == '__main__':
    try:
        # Move the first robot
        move_robot(-0.008315, -5.282071, 0.0, "robot1")
       
        rospy.sleep(3)

        # Move the second robot
        move_robot(2.248869, 6.635135, 1.962612, "robot2")

        # Wait for the first robot to finish
        rospy.sleep(2)

        # Move the first robot again
        move_robot(-4.572061, 3.908484, -3.128271, "robot1")
        rospy.sleep(2)

        # Move the second robot again
        move_robot(0.0, 0.0, -1.57, "robot3")
        rospy.sleep(5)

    except rospy.ROSInterruptException:
        pass

