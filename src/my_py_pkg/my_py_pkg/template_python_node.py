#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyCustomNode(Node): # inherit from the Node parent class so that we can use ROS functionality and methods (e.g. get_logger())
    #constructor 
    def __init__(self): 
        super().__init__("node_name") # run the constructor of the parent class ('Node' in this case) 

def main(args=None):
    rclpy.init(args=args)
    node = MyCustomNode() # MODIFY NAME
    rclpy.spin(node) # keeps the node alive, instead of exiting as soon as its code runs
    rclpy.shutdown()

# useful for running the program directly from the terminal
if __name__ == "__main__":
    main()

    