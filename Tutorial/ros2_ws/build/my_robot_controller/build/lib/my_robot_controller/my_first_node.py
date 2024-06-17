#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#class Node
class MyNode(Node):

    # constructor
    def __init__(self):
        super().__init__("first_node")  #first_node is the name that we are going to run in the graph
        self.get_logger().info("Hello from ROS2")   #writting log in ROS2. Same as Serial printLn

def main(args=None):
    rclpy.init(args=args)   #initialize ros2 communications
    node = MyNode() #To init ROS2 comunications
    rclpy.spin(node)    #allows the node to run continuously
    
    rclpy.shutdown()    #To shutdown ros2 communications. destroy the node

#Usefull for directly executing file from the terminal
if __name__ == '__main__':
    main()