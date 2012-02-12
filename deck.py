import random #module needed for shuffling cards

#diamonds are 4##, hearts are 3##, spades are 2## and clubs are 1##
packvalues = [401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]

def randomcard(n): #called on to select a random card from a list. Also used for pack 'cutting'
    return random.choice(n)

def whatcard(n): #called on to find real name of a card. args = number of the card
    suitnumber = n / 100
    valuenumber = n % 100
    if suitnumber == 1:
        suit = 'clubs'
    elif suitnumber == 2:
        suit = 'spades'
    elif suitnumber == 3:
        suit = 'hearts'
    elif suitnumber == 4:
        suit = 'diamonds'
    if valuenumber == 1:
        value = 'Ace'
    elif valuenumber == 2:
        value = 'Two'
    elif valuenumber == 3:
        value = 'Three'
    elif valuenumber == 4:
        value = 'Four'
    elif valuenumber == 5:
        value = 'Five'
    elif valuenumber == 6:
        value = 'Six'
    elif valuenumber == 7:
        value = 'Seven'
    elif valuenumber == 8:
        value = 'Eight'
    elif valuenumber == 9:
        value = 'Nine'
    elif valuenumber == 10:
        value = 'Ten'
    elif valuenumber == 11:
        value = 'Jack'
    elif valuenumber == 12:
        value = 'Queen'
    elif valuenumber == 13:
        value = 'King'
    print value + ' of ' + suit

def deal(n):
    return n.pop()
