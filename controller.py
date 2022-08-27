from perfect_song import perfect_notes
from instrument import Xylophone
import _thread as thread
import sys
if __name__ == '__main__':
    instrument = Xylophone()

    try:
        thread.start_new_thread( instrument.play, (perfect_notes, ) )
    except Exception as e:
        print("Error:")
        print(e)

    while 1:
        print("Instrument is paused.")
        val = input("\n Press 1 to increase tempo \n Press 2 to decrease tempo \n Press 3 to pause instrument \n Press 4 to resume instrument \n Press 5 to play the song again \n Press 0 to exit\n")
        try:
            val = int(val)
        except:
            val = 100

        if val == 1:
            instrument.increaseTempo()
        elif val == 2:
            instrument.decreaseTempo()
        elif val == 3: 
            instrument.pause()
        elif val == 4:
            instrument.resume()
        elif val == 5:
            thread.start_new_thread( instrument.play, (perfect_notes, ) )
        elif val == 0:
            sys.exit(0)
        else:
            print("Not a valid input.")
