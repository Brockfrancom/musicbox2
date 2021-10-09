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
        'B4':'16',
        'C4':'17',
        'G#1':'18',
        'A#2':'19',
        'C#2':'20',
        'D#2':'21',
        'F#2':'22',
        'G#2':'23',
        'A#3':'24',
        'C#3':'25',
        'D#3':'26',
        'F#3':'27',
        'G#3':'28',
        'A#4':'29'
        }

## To play a song, the sheet music needs to be translated to note objects. 
perfect_notes = []
high_notes = [
    Note(notes['D#2'], 1),
    Note(notes['G2'], 1),
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
    Note(notes['C3'], 1),
    Note(notes['C3'], 1),


]

notes2 = [
]

perfect_notes.append(high_notes)
perfect_notes.append(notes2)
