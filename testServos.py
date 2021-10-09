from adafruit_servokit import ServoKit
kit1 = ServoKit(channels=16)
kit2 = ServoKit(channels=16)
import time

config = {
        0: {"start": 30, "stop": 120, "time": .09,},
        1: {"start": 30, "stop": 70, "time": .04,},
        2: {"start": 30, "stop": 120, "time": .07,},
        3: {"start": 30, "stop": 100, "time": .05,},
        4: {"start": 30, "stop": 90, "time": .06,},
        5: {"start": 30, "stop": 80, "time": .04,},
        6: {"start": 30, "stop": 100, "time": .04,},
        7: {"start": 30, "stop": 80, "time": .06,},
        8: {"start": 30, "stop": 100, "time": .06,},
        9: {"start": 30, "stop": 100, "time": .06,},
        10: {"start": 30, "stop": 100, "time": .06,},
        11: {"start": 30, "stop": 100, "time": .06,},
        12: {"start": 30, "stop": 100, "time": .06,},
        13: {"start": 30, "stop": 100, "time": .06,},
        14: {"start": 30, "stop": 100, "time": .06,},
        15: {"start": 30, "stop": 100, "time": .06,},
        16: {"start": 30, "stop": 100, "time": .06,},
        17: {"start": 30, "stop": 90, "time": .06,},
        18: {"start": 30, "stop": 100, "time": .06,},
        19: {"start": 30, "stop": 100, "time": .06,},
        20: {"start": 30, "stop": 100, "time": .06,},
        21: {"start": 30, "stop": 100, "time": .06,},
        22: {"start": 30, "stop": 100, "time": .06,},
        23: {"start": 30, "stop": 100, "time": .06,},
        24: {"start": 30, "stop": 100, "time": .06,},
        25: {"start": 30, "stop": 90, "time": .06,},
        26: {"start": 30, "stop": 90, "time": .06,},
        }

def moveup():
    for i in range(0,7):
        if (i % 2) == 0:
            kit1.servo[i].angle = 180
        else:
            kit1.servo[i].angle = 0
    time.sleep(1)
    movedown()
    time.sleep(1)


def movedown():    
    for i in range(0,7):
        if (i % 2) == 0:
            kit1.servo[i].angle = 0
        else:
            kit1.servo[i].angle = 180

def dropBall(j):
    kit1.servo[j].angle = 130
    time.sleep(.04)
    kit1.servo[j].angle = 180

def dropBall2(j):
    if j < 16:
        kit1.servo[j].angle = config[j]["stop"]
        time.sleep(config[j]["time"])
        kit1.servo[j].angle = config[j]["start"]
    else:
        kit2.servo[j].angle = config[j]["stop"]
        time.sleep(config[j]["time"])
        kit2.servo[j].angle = config[j]["start"]



#moveup()
#movedown()

j = 15
while True:
    i = input("press enter to drop ball: ")
    if i == "":
        dropBall2(j)
        j += 1


