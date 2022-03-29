#!/usr/bin/env python

"""
I am starting to write code that can be used to check if a sentence provided is grammatically correct.
Please excuse my 'notes' that I write on here...They help me gather more info on the subject since I don't have 
a computer of my own therefore, my code goes hand in hand with the notes for now (changes are upcoming later 😊)
"""


class Grammar:
    __words = []
    _min_length = 1
    
    def __init__(self, line):
        self.line = line
        if len(self.line) < Grammar._min_length:
            raise ValueError('Please check your sentence length!')
        else:
            self.line = line
            
    def break_line(self):
        for x in self.line.split():
            Grammar.__words.append(x)
    
class PartsOfSpeech(Grammar):
    """Nouns, pronouns, Verbs, adjectives, adverbs, prepositions, conjunctions, interjections.
    Some words (adjectives, adverbs, interjections, nouns, verbs) are productive classes allowing new members; 
    others, with functional rather than lexical meaning (articles, conjunctions, prepositions) are nonproductive 
    and have a limited number of members.
    Some grammarians consider articles, quantifiers, and numerals to also be parts of speech.
    
    The basic parts of a sentence are the subject, the verb, and (often, but not always) the object. 
    The subject is usually a noun — a word that names a person, place, or thing. 
    The verb (or predicate) usually follows the subject and identifies an action or a state of being. 
    An object receives the action and usually follows the verb.
    
    
    """
    pass


q = 'This is awesome!'
app = Grammar(q)
print(app.break_line())

