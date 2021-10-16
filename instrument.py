from time import sleep
from adafruit_servokit import ServoKit
import json
kit1 = ServoKit(channels=16, frequency=200)
kit2 = ServoKit(channels=16, address=0x41, frequency=200)

with open('config.json') as f:
    data = f.read()
config = json.loads(data)

class Xylophone:
    def __init__(self):
        self.BPM = 60
        self._pause = True
        self.beat_time = 60/self.BPM

    def play(self, notes):
        for noteOb in notes:
            while self._pause:
                sleep(1)

            if noteOb.note == 'R':
                wait_time_seconds = self.beat_time*noteOb.length
                sleep(wait_time_seconds)
                continue

            self.dropBall(noteOb.note)
            wait_time_seconds = self.beat_time*noteOb.length
            sleep(wait_time_seconds)

    def dropBall(self, note):
        intNote = int(note)
        if intNote <= 15:
            kit1.servo[intNote].angle = 120
            sleep(.04)
            kit1.servo[intNote].angle = int(config[note]["start"])
        else:
            kit2.servo[intNote-16].angle = 120
            sleep(.04)
            kit2.servo[intNote-16].angle = int(config[note]["start"])

    def increaseTempo(self):
        self.BPM += 10
        print("Tempo is now {}".format(self.BPM))

    def decreaseTempo(self):
        if self.BPM > 10:
            self.BPM -= 10
            print("Tempo is now {}".format(self.BPM))
        else:
            print("Tempo cannot be decreased.")

    def pause(self):
        self._pause = True
    
    def resume(self):
        self._pause = False

