import datetime
import socket
import rclpy
import struct
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from serial import Serial

# Create a serial object: Serial(file handle for an arduino, baud rate)
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
        leftPower = round(data.axes[1] * 250 / 2) # int from 0 to 125 for left talon
        rightPower = round(data.axes[4] * 250 / 2) # int from 0 to 125 for right talon
        leftDir = 0x4C if leftPower >= 0 else 0x6C # 'L' (forward) or 'l' (backward)
        rightDir = 0x52 if rightPower >= 0 else 0x72 # 'R' or 'r'

        # Writes our 4-byte packet over serial
        ser.write(
                struct.pack(
                    ">BBBB", leftDir, int(abs(leftPower)), rightDir, int(abs(rightPower))
                    )
                )

def main(args=None):
    rclpy.init(args=args)
    # Create our /joy listener
    sub = Subscriber()
    rclpy.spin(sub)

if __name__ == '__main__':
    main()
