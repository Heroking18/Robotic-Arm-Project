#!/usr/bin/env python3
import rclpy
from rclpy.node import Node #lib for ros2
from geometry_msgs.msg import Twist #lib for moving turtle

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) # publisher. "/turtle1/cmd_vel" is the topic
        self.timer_ = self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Draw circle node has been started")   #writting log in ROS2. Same as Serial printLn

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)   # publish message

def main(args=None):
    rclpy.init(args=args)   #initialize ros2 communications
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()    #To shutdown ros2 communications. destroy the node