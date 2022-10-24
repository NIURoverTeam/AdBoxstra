# ExArca

The NIU Ex Arca integrated ROS2 package

## Rover Data Flow Diagram

This diagram is a WIP draft of our rover's data flow. White elements are stuff that we code, and gray elements are stuff that other subteams (i.e. electrical, science task) code.

![Rover Data Flow Diagram](https://github.com/NIURoverTeam/ExArca/blob/main/exarca_data_flow_diagram_2022.drawio.png)

## Launching the Basic Drive Control Code

On the Arduino:
1. Flash the Arduino with [`Base_Control.ino`](https://github.com/NIURoverTeam/Electrical_Firmware/blob/master/Base_Control/Base_Control.ino)
1. Connect either some spare motors (if testing) or the rover's drive train to the Arduino pins according to what is in the `Base_Control.ino` code.

Then, on the Jetson Nano:
1. Connect the Arduino board to the Jetson Nano using USB, and a controller to the Jetson Nano as well. 
   1. Remote control via the base station and antenna comms is still WIP, for now you'll just have to connect the controller to the rover's Jetson Nano directly.
3. `$ pip3 install pyserial` (Python doesn't have the `serial` module by default, which is needed for the serial communication to the Arduino that our ROS2 [`drive_control_serial.py`](https://github.com/NIURoverTeam/ExArca/blob/main/ex_arca/drive_control_serial.py) file does)
4. `$ sudo chmod 666 /dev/ttyACM0` (this avoids the issue of "permission denied" when trying to write data to `/dev/ttyACM0`, the file handle representing the Arduino)
5. In the root of your workspace: `$ colcon build` to build your workspace
6. In the root of your workspace, but in a new terminal: `$ source install/setup.bash` to source the overlay
7. In that overlay terminal, `$ ros2 launch ex_arca drive_control.launch.py`
   1. If you get any errors, read what they say! It'll help in debugging.
8. If you received no errors, you should be able to operate the motors using the joysticks on the controller.
