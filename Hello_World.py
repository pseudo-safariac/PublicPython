#!/usr/bin/env python
import string


"""
this are the many ways I could think of saying Hello World in Python. 
It is my sole mission and purpose to add as many ways as I can creatively think of.
"""

__author__ = "Kevin Ngigi"
__copyright__ = "Copyright (C) 2022 Kevin Ngigi"
__license__ = "Apache License 2.0"
__maintainer__ = "Kevin Ngigi"
__email__ = "kevinngigi110@gmail.com"


class Game:
    def __init__(self, word):
        self.word = word
        
    def vanilla_word(self):
        return self.word
        
    def underlining_word(self):
        return f'\033[4m {self.word}'
	
	def string_module(word):
    #using the random function
    holding_variable = []
    small = string.ascii_letters
    punctuation = string.punctuation
    for x in word:
        if x in small or punctuation:
            holding_variable.append(x)
        else:
            return f'{x} is not'
    return ''.join(holding_variable)
        
if __name__ == '__main__':
    user_input = 'Hello World!'
    app = Game(user_input)
