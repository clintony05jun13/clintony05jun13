""" TABLE SPECIFIC PARAMETERS

"""
#In Evergreen - right most table = 12
#In Saratoga - at entrance left table = 15
max_black_color_reflection = 15

min_white_color_reflection = 60
PK_straight = 1
PK_turn = 1


""" System Files """
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Icon, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

""" Our files """

""" Get all the functions from our Library
    """
from MineStemLib import resetHeading
from MineStemLib import myHeading

from RobotHeart import RobotHeart
from DudeWhoWillRunMyAssignments import DudeWhoWillRunMyAssignments
from RobotAssignment import RobotAssignment
from RobotRun1 import RobotRun1

""" General notes on coding for FLL robots
    1. Stable straight speed: 200 with acceleration and deceleration of 100
        It will go at 200mm/s and will accelerate at 100 mm/s2
        and decelerate at 100 mm/s2
    2. Stable turn speed: 50 with 0 acceleration
    3. Fast return to home speed: 500 with accleration 100 
    """


myPrimeHub = PrimeHub()
myStopWatch = StopWatch()
myTotalRunTime = StopWatch()
myRobotHeart = RobotHeart()
doTulip = True
myDudeWhoWillRunMyAssignments = DudeWhoWillRunMyAssignments

left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
left_attachment_motor = Motor(Port.C)
right_attachment_motor = Motor(Port.D)

""" LEFT ATTACHMENT
    1. Speed in degrees/s
    1. Angle of rotation in degrees. Positive angle means clockwise
"""
def leftAttachment(speed,angle):
    left_attachment_motor.run_angle(speed,angle,then=Stop.COAST,wait=True)

def rightAttachment(speed,angle):
    right_attachment_motor.run_angle(speed,angle,then=Stop.COAST,wait=True)

#Diameter of the wheels in mm
wheel_dia = 49.5
#The wheels axle track size. This is the distance in mm between the
#two points where both the wheels touch the ground
wheel_axle_dist = 120
drive_base = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=wheel_dia, axle_track=wheel_axle_dist)
drive_base.use_gyro(True)
#left_color_sensor = ColorSensor(Port.E)
#right_color_sensor = ColorSensor(Port.F)

""" Find Line
"""
def findBlackLine(color_sensor):
    drive_base.drive(100,0)
    reading_count = 1
    while True:
        cur_reflection = color_sensor.reflection()
        """
        reading_count = reading_count + 1
        print(reading_count)
        print(":")
        print(cur_reflection)
        print("\n")
        """
        if (cur_reflection < max_black_color_reflection):
            #print(cur_reflection)
            drive_base.stop()
            break
    wait(100)

""" Menu
"""
pressed = []
run_number = 1
myPrimeHub.display.char(str(run_number))
last_buttons = ()

#Run 1
def run1():
    drive_base.settings(straight_speed=800,straight_acceleration=300,turn_rate=400, turn_acceleration=300)
    resetHeading(myPrimeHub) #resets Yaw to 0
    #drive_base.straight(120, then=Stop.COAST)
    #drive_base.turn(-20,then=Stop.COAST)
    #leftAttachment(50, 180)

    

#Run 2
def run2():
    drive_base.settings(straight_speed=800,straight_acceleration=300,turn_rate=400, turn_acceleration=300)
    resetHeading(myPrimeHub) #resets Yaw to 0
    #drive_base.straight(120, then=Stop.COAST)
    #drive_base.turn(-20,then=Stop.COAST)
    #leftAttachment(50, 180)
    
    

#Run 3
def run3():
    drive_base.settings(straight_speed=800,straight_acceleration=300,turn_rate=400, turn_acceleration=300)
    resetHeading(myPrimeHub) #resets Yaw to 0
    #drive_base.straight(120, then=Stop.COAST)
    #drive_base.turn(-20,then=Stop.COAST)
    #leftAttachment(50, 180)



#Run 4
def run4():
    drive_base.settings(straight_speed=800,straight_acceleration=300,turn_rate=400, turn_acceleration=300)
    resetHeading(myPrimeHub) #resets Yaw to 0
    #drive_base.straight(120, then=Stop.COAST)
    #drive_base.turn(-20,then=Stop.COAST)
    #leftAttachment(50, 180)



#Run 5
def run5():
    drive_base.settings(straight_speed=800,straight_acceleration=300,turn_rate=400, turn_acceleration=300)
    resetHeading(myPrimeHub) #resets Yaw to 0
    #drive_base.straight(120, then=Stop.COAST)
    #drive_base.turn(-20,then=Stop.COAST)
    #leftAttachment(50, 180)



#Run 6
def run6():
    drive_base.settings(straight_speed=800,straight_acceleration=300,turn_rate=400, turn_acceleration=300)
    resetHeading(myPrimeHub) #resets Yaw to 0
    #drive_base.straight(120, then=Stop.COAST)
    #drive_base.turn(-20,then=Stop.COAST)
    #leftAttachment(50, 180)
    




""" Permanent loop to process any button that is pressed """
while True:
    buttons = myPrimeHub.buttons.pressed()
    released_buttons = set(last_buttons) - set(buttons)

    """ Process the button that was pressed """
    if (Button.LEFT in released_buttons):
        run_number = run_number + 1
        if run_number > 9:
            run_number = 1
        myPrimeHub.display.char(str(run_number))
    
    if (Button.RIGHT in released_buttons):
        if run_number == 1:
                run1()
                run_number = run_number + 1
                myPrimeHub.display.char(str(run_number))
        elif run_number == 2:
                run2()
                run_number = run_number + 1
                myPrimeHub.display.char(str(run_number))
        elif run_number == 3:
                run3()
                run_number = run_number + 1
                myPrimeHub.display.char(str(run_number))
        elif run_number == 4:
                run4()
                run_number = run_number + 1
                myPrimeHub.display.char(str(run_number))
        elif run_number == 5:
                run5()
                run_number = run_number + 1
                myPrimeHub.display.char(str(run_number))
        elif run_number == 6:
                run6()
                run_number = 1
                myPrimeHub.display.char(str(run_number))

    last_buttons = buttons
