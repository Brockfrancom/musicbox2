class Note:
    ## 'B4':'16', # bigger instrument has this note.
    ## 'C4':'17', # bigger instrument has this note.
    ## 'A#4':'29' # bigger instrument has this note.
    XYLOPHONE_NOTE_SERVO = {
        'G1':'0',
        'A2':'1',
        'B2':'2',
        'C2':'3',
        'D2':'4',
        'E2':'5',
        'F2':'6',
        'G2':'7',
        'A3':'8',
        'B3':'9',
        'C3':'10',
        'D3':'11',
        'E3':'12',
        'F3':'13',
        'G3':'14',
        'A4':'15',
        'G#1':'16',
        'A#2':'17',
        'C#2':'18',
        'D#2':'19',
        'F#2':'20',
        'G#2':'21',
        'A#3':'22',
        'C#3':'23',
        'D#3':'24',
        'F#3':'25',
        'G#3':'26',
        }

    def __init__(self, note, length):
        self.note = note
        self.length = length
