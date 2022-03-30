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

    def sender_to_partsofspeech(self):
        PartsOfSpeech.nouns(Grammar.__words)
        PartsOfSpeech.pronouns(Grammar.__words)
        PartsOfSpeech.adjectives(Grammar.__words)
        PartsOfSpeech.adverbs(Grammar.__words)
        PartsOfSpeech.prepositions(Grammar.__words)
        PartsOfSpeech.conjunctions(Grammar.__words)
        PartsOfSpeech.interjections(Grammar.__words)


class PartsOfSpeech(Grammar):
    def nouns(self):
        q = self
        return q
    
    def pronouns(self):
        pass
    
    def adjectives(self):
        pass
    
    def adverbs(self):
        pass
    
    def prepositions(self):
        pass
    
    def conjunctions(self):
        pass
    
    def interjections(self):
        pass


class sentenceType(Grammar):
    def simple_sentence(self):
        pass
    
    def compound_sentence(self):
        pass
    
    def complex_senctence(self):
        pass
    
    def  compound_complex_sentence(self):
        pass
 
    # There are four main types of sentences that can be distinguished by their function and purpose:   
    def declarative_sentence(self):
        pass
    
    def interrogative_sentence(self):
        pass
    
    def inperative_sentence(self):
        pass
    
    def exclamatory_sentence(self):
        pass
    

class sentenceAssistance(Grammar):
    def sentence_coordinaters(self):
        pass
    
    def adjective_clauses(self):
        pass
    
    def appositives(self):
        pass
    
    def adverb_clauses(self):
        pass
    
    def participial_phrases(self):
        pass
    
    def absolute_phrases(self):
        pass
    
    
"""Nouns, pronouns, Verbs, adjectives, adverbs, prepositions, conjunctions, interjections.
Some words (adjectives, adverbs, interjections, nouns, verbs) are productive classes allowing new members; 
others, with functional rather than lexical meaning (articles, conjunctions, prepositions) are nonproductive 
and have a limited number of members.
Some grammarians consider articles, quantifiers, and numerals to also be parts of speech.

https://www.thoughtco.com/sentence-parts-and-sentence-structures-1689671
The subject is usually a noun — a word that names a person, place, or thing. 
The verb (or predicate) usually follows the subject and identifies an action or a state of being. 
An object receives the action and usually follows the verb.

"""


if __name__ == '__main__':
    q = 'This is awesome!'
    app = Grammar(q)
    app2 = PartsOfSpeech(q)
    print(app2.nouns())

# This is the format I should use to define sender_to_partsofspeech
    """
class A:
    __d = 'angular momentum'
    def receiver(self):
        print('First call')
        B.sth(A.__d)
        B.ask(A.__d)
        
    def grasper(self):
        q = B.sth(A.__d)
        print(str(q), 'is q without spice')
        


class B(A):
    def sth(self):
        z = self
        print(z, 'is z')
        return z 
        
    def ask(self):
        z1 = self
        print(z1, 'is z1')


q = 'qwerty'
b = B()
a = A()
print(a.grasper())
#print(a.receiver())
"""
