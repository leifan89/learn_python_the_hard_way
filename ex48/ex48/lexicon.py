DIRECTIONS = [
    'north',
    'south',
    'east',
    'west',
    'down',
    'up',
    'left',
    'right',
    'back'
]
DIRECTION = 'direction'

VERBS = [
    'go',
    'stop',
    'kill',
    'eat'
]
VERB = 'verb'

STOPS = [
    'the',
    'in',
    'of',
    'form',
    'at',
    'it'
]
STOP = 'stop'

NOUNS = [
    'door',
    'bear',
    'princess',
    'cabinet'
]
NOUN = 'noun'

NUMBER = 'number'
ERROR = 'error'

def scan(words):
    ret = []
    for word in words.split(' '):
        if word in DIRECTIONS:
            ret.append((DIRECTION, word))
        elif word in VERBS:
            ret.append((VERB, word))
        elif word in STOPS:
            ret.append((STOP, word))
        elif word in NOUNS:
            ret.append((NOUN, word))
        else:
            try:
                number = int(word)
                ret.append((NUMBER, number))
            except ValueError:
                ret.append((ERROR, word))
    return ret