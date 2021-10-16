import sys
import _thread
from piano_song import *
from piano import Piano
from adafruit_servokit import ServoKit

if __name__ == '__main__':
    num_hands = 15
    num_notes = 5000
    num_channels = num_hands*2
    bpm = 80
    kit = ServoKit(channels=16)
    piano = Piano(bpm, num_channels, kit)
    #generateHands(num_notes, num_hands)

    try:
        # for i in range(0,num_hands):
        #     _thread.start_new_thread( piano.play, (rand_notes[i], ) )

        # To play a song, set the variables in piano_song.py to be the notes in order. 
        for i in range(0,len(perfect_notes)):
            _thread.start_new_thread( piano.play, (perfect_notes[i], ) )
    except Exception as e:
        print("Error: unable to start thread")
        print(e)

    while 1:
        val = int(input("\n Press 1 to increase tempo \n Press 2 to decrease tempo \n Press 3 to pause piano \n Press 4 to resume piano \n Press 5 to set number of channels \n Press 0 to exit\n"))
        if val == 1:
            piano.increaseTempo()
        elif val == 2:
            piano.decreaseTempo()
        elif val == 3: 
            piano.pause()
        elif val == 4:
            piano.resume()
        elif val == 0:
            sys.exit(0)
        else:
            print("Not a valid input.")
