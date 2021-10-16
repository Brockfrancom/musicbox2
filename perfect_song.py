from note import Note

notes = {
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

## 'B4':'16', # bigger instrument has this note.
## 'C4':'17', # bigger instrument has this note.
## 'A#4':'29' # bigger instrument has this note.
## https://www.youtube.com/watch?v=Oq5ZPH-r_YY
## To play a song, the sheet music needs to be translated to note objects. 
perfect_notes = [
    Note(notes['D#2'], 1),
    Note(notes['F2'], 1),
    Note(notes['G#2'], 1),
    Note(notes['G#2'], 1),

    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['C3'], 1),
 
    Note(notes['A#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['C3'], 1),
    Note(notes['C3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['G#2'], 1),

    Note(notes['G#2'], 1),
    Note(notes['A#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),

    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['C3'], 1),

    Note(notes['C#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),

    Note(notes['G#2'], 1),

    Note(notes['G#2'], 1),
    Note(notes['A#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['C#3'], 1),
    Note(notes['C#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['G#2'], 1),
    Note(notes['A#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['A#3'], 1), # 30 seconds

    Note(notes['D#3'], 1),
    Note(notes['D#3'], 1),
    Note(notes['D#3'], 1),
    Note(notes['F3'], 1),
    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['C3'], 1),

    Note(notes['C3'], 1),

    Note(notes['C3'], 1),

    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['C3'], 1),

    Note(notes['C3'], 1),
    
    Note(notes['C3'], 1),

    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['C#3'], 1),

    Note(notes['C3'], 1),

    Note(notes['G#2'], 1),

    Note(notes['D#2'], 1), # 43 seconds

    Note(notes['C3'], 1),

    Note(notes['C#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['C3'], 1),

    Note(notes['C3'], 1), # 49 seconds

    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['C3'], 1),

    Note(notes['C3'], 1),

    Note(notes['C3'], 1),

    Note(notes['C3'], 1),
    Note(notes['A#3'], 1),
    Note(notes['G#2'], 1),
    Note(notes['C#3'], 1),

    Note(notes['C3'], 1),

    Note(notes['G#2'], 1),

    Note(notes['D#2'], 1),
    Note(notes['A#3'], 1),
    Note(notes['A#3'], 1),
]

