#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    #constructor 
    def __init__(self): 
        super().__init__("number_publisher")
        self.declare_parameter("number", 2)
        self.declare_parameter("timer_period", 1.0) 
        # self.number_ = 2
        self.number_ = self.get_parameter("number").value
        self.add_post_set_parameters_callback(self.parameters_callback)

        self.timer_period_ = self.get_parameter("timer_period").value
        self.number_publisher_ = self.create_publisher(Int64, "number", 10)
        self.number_timer_ = self.create_timer(self.timer_period_, self.publish_number)
        self.get_logger().info("Number Publisher has been started.")

    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)

    def parameters_callback(self, params: list[Parameter]):
        for param in params:
            if param.name == "number":
                self.number_ = param.value

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode() 
    rclpy.spin(node) # keeps the node alive, instead of exiting as soon as its code runs
    rclpy.shutdown()

# useful for running the program directly from the terminal
if __name__ == "__main__":
    main()

    