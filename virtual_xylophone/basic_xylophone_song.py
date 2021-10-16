from note import Note
import math
import random

def generateNotes():
    randNotes = []
    length = [1/2, 1/4, 1/8]
    notes = [
        'A1','A2','A3','A4','A5','A6','A7',
        'Ab1','Ab2','Ab3','Ab4','Ab5','Ab6','Ab7',
        'B1','B2','B3','B4','B5','B6','B7',
        'Bb1','Bb2','Bb3','Bb4','Bb5','Bb6','Bb7',
        'C1','C2','C3','C4','C5','C6','C7','C8'
        'D1','D2','D3','D4','D5','D6','D7',
        'Db1','Db2','Db3','Db4','Db5','Db6','Db7',
        'E1','E2','E3','E4','E5','E6','E7',
        'Eb1','Eb2','Eb3','Eb4','Eb5','Eb6','Eb7',
        'F1','F2','F3','F4','F5','F6','F7',
        'G1','G2','G3','G4','G5','G6','G7',
        'Gb1','Gb2','Gb3','Gb4','Gb5','Gb6',
        ]
    for i in range(0,50):
        l = random.randint(0,len(length)-1)
        n = random.randint(0,len(notes)-1)
        randNotes.append(Note(notes[n], length[l])
    return randNotes

high_notes = generateNotes()
mid_high_notes = generateNotes()
mid_low_notes = generateNotes()
low_notes = generateNotes()

# high_notes = [
#     Note('1', 1/8), 
#     Note('2', 1/8), 
#     Note('3', 1/8),

#     Note('4', 1/2),
#     Note('5', 1/4),

#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
# ]

# mid_high_notes = [
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
#     Note('6', 1/8), 
#     Note('7', 1/8), 
#     Note('8', 1/8),
# ]

# mid_low_notes = [
#     Note('2', 1/8), 
#     Note('3', 1/8),

#     Note('4', 1/2),
#     Note('5', 1/4),
#     Note('4', 1/2),
# ]

# low_notes = [
#     Note('1', 1/8), 
#     Note('2', 1/8), 
#     Note('3', 1/8),

#     Note('4', 1/2),
#     Note('5', 1/4),
#     Note('1', 1/8), 
#     Note('2', 1/8), 
#     Note('3', 1/8),

#     Note('4', 1/2),
#     Note('5', 1/4),
# ]
