#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    #constructor 
    def __init__(self): 
        super().__init__("number_counter") 
        self.counter_ = 0
        self.number_count_publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.number_subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        # self.timer = self.create_timer(1, self.publish_number)
        self.reset_counter_service_ = self.create_service(SetBool, "reset_counter", self.callback_reset_counter)

        self.get_logger().info("Number Counter has been started.")

    def callback_number(self, msg: Int64):
        # self.get_logger().info(str(msg.data)) # for testing purposes
        self.counter_ += msg.data

        # publishing from within the same callback method, instead of using a timer in the constructor. Publish as soon as data is received - makes sense (becomes a data pipeline)
        new_msg = Int64()
        new_msg.data = self.counter_
        self.number_count_publisher_.publish(new_msg)

    def callback_reset_counter(self, request: SetBool.Request, response: SetBool.Response):
        if request.data:
            self.counter_ = 0
            response.success = True
            response.message = "Counter has been reset"
        else:
            response.success = False
            response.message = "Counter has not been reset"

        return response


    # def publish_number(self):
    #     number = Int64()
    #     number.data = self.counter
    #     self.publisher_.publish(number)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node) # keeps the node alive, instead of exiting as soon as its code runs
    rclpy.shutdown()

# useful for running the program directly from the terminal
if __name__ == "__main__":
    main()

    