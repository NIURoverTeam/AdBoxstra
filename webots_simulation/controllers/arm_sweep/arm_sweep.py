"""Sweeps through range of motion for all arm joints."""

# imports from the controller module
from controller import Robot
from controller import Motor
from enum import Enum

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# initialize and enable sensors and motors
armAxes = [] # axes of arm (some slider joints, some hinge joints)
armAxesNames = ['arm_axis1_transl', 'arm_axis2_rot',
                'arm_axis3_transl', 'arm_axis4_rot',
                'arm_axis5_rot']
for i in range(len(armAxesNames)):
    armAxes.append(robot.getDevice(armAxesNames[i]))
    armAxes[i].setPosition(0.0)
    # armAxes[i].setVelocity(0.0)

rotAxisMinAngle = -1.57 # -pi/2
rotAxisMaxAngle = 1.57  # pi/2
rotAxisChangeRate = 0.04 # radians/step

axis1ChangeRate = 0.005 # meters/step
axis2ChangeRate = rotAxisChangeRate
axis3ChangeRate = 0.005 # meters/step
axis4ChangeRate = rotAxisChangeRate
axis5ChangeRate = rotAxisChangeRate

axis1MinStop = -0.2
axis2MinStop = rotAxisMinAngle
axis3MinStop = -0.1
axis4MinStop = rotAxisMinAngle
axis5MinStop = rotAxisMinAngle

axis1MaxStop = 0.0
axis2MaxStop = rotAxisMaxAngle
axis3MaxStop = 0.0
axis4MaxStop = rotAxisMaxAngle
axis5MaxStop = rotAxisMaxAngle

axis1StartPos = 0.0
axis2StartPos = 0.0
axis3StartPos = 0.0
axis4StartPos = 0.0
axis5StartPos = 0.0

axis1Pos = 0.0
axis2Pos = 0.0
axis3Pos = 0.0
axis4Pos = 0.0
axis5Pos = 0.0

class axisDirection(Enum):
    BACK = "backward"
    ZERO = "zero"
    FWD = "forward"

currentAxis = 1  # state to control which axis is sweeping
currentDirection = axisDirection.BACK  # start w/ backwards

def moveAxis(currentAxis, currentDirection, axisPos,
             axisChangeRate, axisStartPos, axisMinStop,
             axisMaxStop):
    '''
    Move the current axis to its min, then its max, and then its
    zero. After that, advance to the next axis.
    '''
    if currentDirection == axisDirection.BACK:
        # go backwards until min stop reached, then go forward
        if axisPos > axisMinStop:
            axisPos -= axisChangeRate
        else:
            currentDirection = axisDirection.FWD
    elif currentDirection == axisDirection.FWD:
        # go forward until max stop reached, then go to zero
        if axisPos < axisMaxStop:
            axisPos += axisChangeRate
        else:
            currentDirection = axisDirection.ZERO
    elif currentDirection == axisDirection.ZERO:
        # go backward until zero reached, then prep for next axis
        if axisPos > axisStartPos:
            axisPos -= axisChangeRate
        else:
            currentDirection = axisDirection.BACK
            if currentAxis < 5:
                currentAxis += 1
            else:
                currentAxis = 1

    armAxes[currentAxis - 1].setPosition(axisPos)
    
    return currentAxis, currentDirection, axisPos

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    if currentAxis == 1:
        currentAxis, currentDirection, axis1Pos = moveAxis(
            currentAxis,
            currentDirection,
            axis1Pos,
            axis1ChangeRate,
            axis1StartPos,
            axis1MinStop,
            axis1MaxStop
        )
    elif currentAxis == 2:
        currentAxis, currentDirection, axis2Pos = moveAxis(
            currentAxis,
            currentDirection,
            axis2Pos,
            axis2ChangeRate,
            axis2StartPos,
            axis2MinStop,
            axis2MaxStop
        )
    elif currentAxis == 3:
        currentAxis, currentDirection, axis3Pos = moveAxis(
            currentAxis,
            currentDirection,
            axis3Pos,
            axis3ChangeRate,
            axis3StartPos,
            axis3MinStop,
            axis3MaxStop
        )
    elif currentAxis == 4:
        currentAxis, currentDirection, axis4Pos = moveAxis(
            currentAxis,
            currentDirection,
            axis4Pos,
            axis4ChangeRate,
            axis4StartPos,
            axis4MinStop,
            axis4MaxStop
        )
    elif currentAxis == 5:
        currentAxis, currentDirection, axis5Pos = moveAxis(
            currentAxis,
            currentDirection,
            axis5Pos,
            axis5ChangeRate,
            axis5StartPos,
            axis5MinStop,
            axis5MaxStop
        )
    else:
        # should be impossible to get here
        assert False, "axis " + str(currentAxis) +  " is invalid"


# Enter here exit cleanup code.
