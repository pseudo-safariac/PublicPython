#!/usr/bin/env python
"""
this are the many ways of creatively saying Hello World in Python. 
It is my sole mission and purpose to add as many ways as I can creatively think of.
"""

print('hello World')  #This is the only one that is unique since it is most famous

	
#print("\033[1;32;40m Bright Green  \n")
class FancyWord:
    def __init__(self, word):
        self.word = word
    
    def underlining_word(self):
        return f'\033[4m {self.word}'
        
    
        

text = 'Hello World'       

first = FancyWord(text)
print(first.underlining_word())
