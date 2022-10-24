from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy_linux',
            executable='joy_linux_node',
            name='joy'
        ),
        Node(
            package='ex_arca',
            executable='drive_control_serial',
            name='drive_control',
            output='screen',
            emulate_tty=True
        )
    ])
