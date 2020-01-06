from .lexicon import scan

class Sentence(object):
    def __init__(self):
        self.subject = "player"
        self.verb = None
        self.object = None
    
    def set_subject(self, subject):
        self.subject = subject

    def set_verb(self, verb):
        self.verb = verb
    
    def set_object(self, object):
        self.object = object
    

class ParserError(Exception):
    pass

# Assumes subject-verb-object construction
# First noun is assumed to be the subject
# Noun is assumed to be immediately followed by verb
# First noun following verb is assumed to be the object
# A sentence is assumed to have no more than 1 subject
# A sentence is assumed to have exactly 1 verb
# A sentence is assumed to have no more than 1 object
def parser(sentence):
    verb_seen = False
    result = scan(sentence)
    sentence = Sentence()
    index = 0
    while index < len(result):
        if not verb_seen:   # no verb yet, look for subject or verb
            if result[index][0] != 'noun' and result[index][0] != 'verb':
                index += 1
                continue
            if result[index][0] == 'noun':     # subject
                if index + 1 >= len(result):
                    raise ParserError('Sentence does not contain a verb!')
                next_word_tuple = result[index+1] 
                if (next_word_tuple[0] != 'verb'):
                    raise ParserError('Verb must immediately follow subject!')
                sentence.set_subject(result[index][1])
                sentence.set_verb(next_word_tuple[1])
                verb_seen = True
                index += 2  # skip the verb
            else:
                sentence.set_verb(result[index][1])
                verb_seen = True
                index += 1
        else:
            if result[index][0] != 'noun' and result[index][0] != 'direction':  # assume object can be noun or direction
                index += 1
                continue
            sentence.set_object(result[index][1])
            return sentence # once we have object, just finish
    return sentence

parser("princess kill")