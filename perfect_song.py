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
    Note(notes['D#2'], 1/2), # I 
    Note(notes['F2'], 1/2),  # found
    Note(notes['G#2'], 1/8), # a 
    Note(notes['G#2'], 3),   # love

    Note(notes['C3'], 1),    # for
    Note(notes['A#3'], 1/2), 
    Note(notes['G#2'], 1/2),
    Note(notes['C3'], 3),    # me
 
    Note(notes['A#3'], 1),   # darl
    Note(notes['C3'], 1),    # ing
    Note(notes['C3'], 1),    # just 
    Note(notes['C3'], 1),    # dive
    Note(notes['G#2'], 1),   # right
    Note(notes['G#2'], 1),   # in

    Note(notes['G#2'], 1),   # foll-
    Note(notes['A#3'], 1),   # ow
    Note(notes['C3'], 1),    # my
    Note(notes['A#3'], 1),   # lead

    Note(notes['C3'], 1),    # I
    Note(notes['A#3'], 1),   # found
    Note(notes['G#2'], 1),   # a
    Note(notes['C3'], 1),    # girl 

    Note(notes['C#3'], 1),   # beau-
    Note(notes['C3'], 1),    # ti-
    Note(notes['A#3'], 1),   # ful
    Note(notes['G#2'], 1),   # and

    Note(notes['G#2'], 1),   # sweet

    Note(notes['G#2'], 1),   # I
    Note(notes['A#3'], 1),   # nev-
    Note(notes['C3'], 1),    # ver
    Note(notes['C#3'], 1),   # knew
    Note(notes['C#3'], 1),   # you
    Note(notes['C3'], 1),    # were
    Note(notes['A#3'], 1),   # the
    Note(notes['A#3'], 1),   # some-
    Note(notes['G#2'], 1),   # one
    Note(notes['G#2'], 1),   # wait-
    Note(notes['A#3'], 1),   # ing
    Note(notes['C3'], 1),    # for
    Note(notes['A#3'], 1),   # me      30 seconds

    Note(notes['D#3'], 1),   # We
    Note(notes['D#3'], 1),   # were
    Note(notes['D#3'], 1),   # just
    Note(notes['F3'], 1),    # kids
    Note(notes['C3'], 1),    # when
    Note(notes['A#3'], 1),   # we
    Note(notes['C3'], 1),    # fell

    Note(notes['C3'], 1),    # in

    Note(notes['C3'], 1),    # love

    Note(notes['C3'], 1),    # not
    Note(notes['A#3'], 1),   # know-
    Note(notes['G#2'], 1),   # ing
    Note(notes['C3'], 1),    # what

    Note(notes['C3'], 1),    # it
    
    Note(notes['C3'], 1),    # was

    Note(notes['C3'], 1),    # I
    Note(notes['A#3'], 1),   # will
    Note(notes['G#2'], 1),   # not
    Note(notes['C#3'], 1),   # give

    Note(notes['C3'], 1),    # you

    Note(notes['G#2'], 1),   # up

    Note(notes['D#2'], 1),   # this   43 seconds

    Note(notes['C3'], 1),    # ti-

    Note(notes['C#3'], 1),   # i-
    Note(notes['C3'], 1),    # i-
    Note(notes['A#3'], 1),   # me
    Note(notes['C3'], 1),    # Darl-
    Note(notes['A#3'], 1),   # ing
    Note(notes['G#2'], 1),   # just
    Note(notes['C3'], 1),    # kiss

    Note(notes['C3'], 1),    # me    49 seconds

    Note(notes['C3'], 1),    # slow
    Note(notes['A#3'], 1),   # your
    Note(notes['G#2'], 1),   # heart
    Note(notes['C3'], 1),    # is

    Note(notes['C3'], 1),    # all

    Note(notes['C3'], 1),    # I

    Note(notes['C3'], 1),    # own
    Note(notes['A#3'], 1),   # and
    Note(notes['G#2'], 1),   # in
    Note(notes['C#3'], 1),   # your

    Note(notes['C3'], 1),    # eyes

    Note(notes['G#2'], 1),   # your

    Note(notes['D#2'], 1),   # hold-
    Note(notes['A#3'], 1),   # ing
    Note(notes['A#3'], 1),   # mine
]

