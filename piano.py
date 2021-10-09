import pygame
from time import sleep

class Piano:
    def __init__(self, bpm, num_channels, kt):
        self.BPM = bpm
        self._pause = False
        self.kit = kt

    def play(self, notes):
        for noteOb in notes:
            while self._pause:
                sleep(1)

            if noteOb.note == 'R':
                beat_time = 60/self.BPM
                wait_time_seconds = beat_time*noteOb.length
                sleep(wait_time_seconds)
                continue

            beat_time = 60/self.BPM
            self.dropBall(int(noteOb.note))
            wait_time_seconds = beat_time*noteOb.length
            sleep(wait_time_seconds)

    def dropBall(self, note):
        self.kit.servo[note].angle = 130
        sleep(.04)
        self.kit.servo[note].angle = 180

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

