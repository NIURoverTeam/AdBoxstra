"""four_wheeled_collision_avoidance controller."""

# imports from the controller module
from controller import Robot
from controller import Motor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# initialize and enable snesors and motors
ds = [] # distance sensors
dsNames = ['ds_right', 'ds_left']
for i in range(len(dsNames)):
    ds.append(robot.getDevice(dsNames[i])) # initialize distance sensors
    ds[i].enable(timestep)
wheels = []
wheelsNames = ['left_wheel1', 'right_wheel1',
               'left_wheel2', 'right_wheel2',
               'left_wheel3', 'right_wheel3']
for i in range(len(wheelsNames)):
    wheels.append(robot.getDevice(wheelsNames[i])) # initialize motors
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
    
avoidObstacleCounter = 0
baseSpeed = 3.0
leftSpeed = baseSpeed
rightSpeed = baseSpeed

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # determine the new speeds based on sensor feedback
    if avoidObstacleCounter > 90:
        # if obstacle just detected, back up a bit so there's
        # room to turn
        avoidObstacleCounter -= 1
        leftSpeed = -1 * baseSpeed
        rightSpeed = -1 * baseSpeed
        print("backing up...", avoidObstacleCounter)
    elif avoidObstacleCounter > 0:
        # after backing up, turn
        avoidObstacleCounter -= 1
        turningSpeedBoost = 2.0  # to overcome static friction
        leftSpeed = 1 * baseSpeed * turningSpeedBoost
        rightSpeed = -1 * baseSpeed * turningSpeedBoost
        print("turn...", avoidObstacleCounter)
    elif avoidObstacleCounter <= 0:
        leftSpeed = baseSpeed
        rightSpeed = baseSpeed
        print("no turning", avoidObstacleCounter)
        
        # if either distance sensor is triggered, begin turning
        for i in range(2):
            if ds[i].getValue() < 950.0:
                print("turning!")
                avoidObstacleCounter = 100
    
    # write the speeds to the motors
    print(leftSpeed, ", ", rightSpeed)
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    wheels[4].setVelocity(leftSpeed)
    wheels[5].setVelocity(rightSpeed)

# Enter here exit cleanup code.
