import random #module needed for shuffling cards

diamonds = [401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413]
hearts = [301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313]
spades = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213]
clubs = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]

pack = [diamonds + hearts + spades + clubs] #defines pack as sum of all cards

print random.shuffle(pack,random.random) #prints the shuffled pack
print pack
raw_input()
