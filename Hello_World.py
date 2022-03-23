#!/usr/bin/env python

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
        
if __name__ == '__main__':
    user_input = 'Hello World!'
    app = Game(user_input)
