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
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
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
    if avoidObstacleCounter > 0:
        # object detected, so turn
        avoidObstacleCounter -= 1
        leftSpeed = 1 * baseSpeed
        rightSpeed = -1 * baseSpeed
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

# Enter here exit cleanup code.
