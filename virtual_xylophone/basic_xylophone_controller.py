import pygame
import _thread
from basic_xylophone_song import *

BPM = 50

def play(notes):
    pygame.mixer.init()
    beat_time = 60/BPM
    for noteOb in notes:
        my_sound = pygame.mixer.Sound('basic_xylophone/' + noteOb.note + '.wav')
        my_sound.play()
        pygame.time.wait(int(beat_time*(noteOb.length)*1000)) 


if __name__ == '__main__':
    try:
        _thread.start_new_thread( play, (high_notes, ) )
        _thread.start_new_thread( play, (mid_high_notes, ) ) 
        _thread.start_new_thread( play, (mid_low_notes, ) )
        _thread.start_new_thread( play, (low_notes, ) ) 
    except Exception as e:
        print("Error: unable to start thread")
        print(e)
    
    while 1:
        pass
