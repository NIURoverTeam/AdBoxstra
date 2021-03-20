import datetime
import socket
import rclpy
import struct
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from serial import Serial

ser = Serial("/dev/ttyACM0", 9600)

class Subscriber(Node):
    def __init__(self):
        super().__init__('drive_control_serial')
        self.subscription = self.create_subscription(
                Joy,
                'joy',
                self.on_joy_msg,
                10)
        self.subscription # prevent unused variable warning

    def on_joy_msg(self, data):
        leftPower = round(data.axes[1] * 250 / 2)
        rightPower = round(data.axes[4] * 250 / 2)
        leftDir = 0x4C if leftPower >= 0 else 0x6C
        rightDir = 0x52 if rightPower >= 0 else 0x72

        ser.write(
                struct.pack(
                    ">BBBB", leftDir, int(abs(leftPower)), rightDir, int(abs(rightPower))
                    )
                )

def main(args=None):
    rclpy.init(args=args)
    sub = Subscriber()
    rclpy.spin(sub)

if __name__ == '__main__':
    main()
