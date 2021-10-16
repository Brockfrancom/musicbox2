from perfect_song import perfect_notes
from instrument import Xylophone
import _thread
import sys
if __name__ == '__main__':
    instrument = Xylophone()

    try:
        _thread.start_new_thread( instrument.play, (perfect_notes, ) )
    except Exception as e:
        print("Error:")
        print(e)

    while 1:
        val = int(input("\n Press 1 to increase tempo \n Press 2 to decrease tempo \n Press 3 to pause instrument \n Press 4 to resume instrument \n Press 5 to play the song again \n Press 0 to exit\n"))
        if val == 1:
            instrument.increaseTempo()
        elif val == 2:
            instrument.decreaseTempo()
        elif val == 3: 
            instrument.pause()
        elif val == 4:
            instrument.resume()
        elif val == 5:
            _thread.start_new_thread( instrument.play, (perfect_notes, ) )
        elif val == 0:
            sys.exit(0)
        else:
            print("Not a valid input.")
