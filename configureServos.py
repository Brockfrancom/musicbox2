from adafruit_servokit import ServoKit
import time
import json
kit1 = ServoKit(channels=16, frequency=200)
kit2 = ServoKit(channels=16, address=0x41, frequency=200)

with open('config.json') as f:
    data = f.read()
config = json.loads(data)

def dropBall(j):
    integerJ = int(j)
    if integerJ <= 15:
        kit1.servo[integerJ].angle = int(config[j]["stop"])
        time.sleep(float(config[j]["time"]))
        kit1.servo[integerJ].angle = int(config[j]["start"])
    else:
        kit2.servo[integerJ-16].angle = int(config[j]["stop"])
        time.sleep(float(config[j]["time"]))
        kit2.servo[integerJ-16].angle = int(config[j]["start"])


def calibrate():
    while True:
        try:
            i = int(input("Select servo: "))
            print("Angle is currently " + str(config[str(i)]["start"]))
            newAngle = input("Select angle or t to test: ")
            if newAngle =="t":
                dropBall(str(i))
                continue
            newAngle = int(newAngle)
            config[str(i)]["start"] = newAngle
            if i <= 15:
                kit1.servo[i].angle = newAngle
            else:
                kit2.servo[i-16].angle = newAngle
        except Exception as e:
            print(e)
            with open('config.json', 'w') as fp:
                json.dump(config, fp)
            break

def test():
    while True:
        try:
            i = int(input("Select servo: "))
            dropBall(str(i))
        except Exception as e:
            print(e)
            break

def dropQuick():
    for i in range(0,25):
        dropBall("2")
        time.sleep(.4)

def dropAll():
    for i in range(0, 27):
        dropBall(str(i))
        time.sleep(.3)

i = int(input("Press\n1 to calibrate \n2 to test\n3 to drop quick\n4 to drop all \n"))
if i == 1:
    calibrate()
if i == 2:
    test()
if i == 3:
    dropQuick()
if i == 4:
    dropAll()
