import os
import pathlib
import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher


def generate_launch_description():
    package_dir = get_package_share_directory('AdBoxtra')  # FIXME or should it be 'ad_boxtra'?
    robot_description = pathlib.Path(os.path.join(package_dir, 'resource', 'my_robot.urdf')).read_text()

    # this action will launch a webots simulation instance
    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'webots_simulation/worlds', 'adboxtra_2022_simplified.wbt')
    )

    # this node interacts with a robot in the webots simulation
    my_robot_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        parameters=[
            {'robot_description': robot_description},
        ]
    )

    return LaunchDescription([
        webots, # start the webots node
        my_robot_driver,    # start the webots robot driver
        launch.actions.RegisterEventHandler(    # this action will kill all nodes once
                                                # the webots simulation has exited
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
