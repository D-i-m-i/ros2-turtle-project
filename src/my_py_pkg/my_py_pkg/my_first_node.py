#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    #constructor 
    def __init__(self): 
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello World")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello Yeaahhhh" + str(self.counter_))
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) # keeps the node alive, instead of exiting as soon as its code runs
    rclpy.shutdown()

# useful for running the program directly from the terminal
if __name__ == "__main__":
    main()

    