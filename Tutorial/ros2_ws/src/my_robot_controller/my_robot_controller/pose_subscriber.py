#!/usr/bin/env python3
import rclpy
from rclpy.node import Node #lib for ros2
from turtlesim.msg import Pose  #lib for moving the position of the turtle

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subcriber")
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10) #subcribing to topic turtle1/pose

    def pose_callback(self, msg: Pose):
        self.get_logger().info("(" + str(msg.x) + ", " + str(msg.y) + ")")

def main(args=None):
    rclpy.init(args=args)   #initialize ros2 communications
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()    #To shutdown ros2 communications. destroy the node