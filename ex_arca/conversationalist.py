import datetime
import socket
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__('conversationalist')
        self.subscription = self.create_subscription(
                String,
                'logger',
                self.listener_callback,
                10)
        self.subscription # prevent unused variable warning

    def listener_callback(self, msg):
        print('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    sub = Subscriber()
    print("+----------------------------------------------------------------------------------+")
    print("|             👋 Hello! My name is Ex Arca, the boxy rover from NIU.               |")
    print("|                                                                                  |")
    print("|                  ⌚ It is currently", datetime.datetime.now(),"                  |")
    print("|                                                                                  |")
    print("|                            🌐 My IP is", socket.gethostbyname(socket.gethostname()),"                               |")
    print("|                                                                                  |")
    print("|             If you want to know more about how to make me do things,             |")
    print("|                  check out https://github.com/NIURoverTeam/Docs                  |")
    print("|                                                                                  |")
    print("| You can help build me at https://niurover.com or https://github.com/NIURoverTeam |")
    print("+----------------------------------------------------------------------------------+")
    print("Now I'm listening to the '/logger' topic. You can publish messages there with:")
    print("ros2 topic pub --once /logger std_msgs/msg/String \"{data: '<your message>'}\"")
    rclpy.spin(sub)

if __name__ == '__main__':
    main()
