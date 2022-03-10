#!/usr/bin/env python
""" This is some code that @AnshSharma from Programming Hero requested some help in.
Its simple and short, it's been made because she/he needed to know how such a program may run

The program is game that is a question that receives one input as an answer.
Correct answers give the user 5 points
"""

__author__ = "Kevin Ngigi"
__copyright__ = "Copyright (C) 2022 Kevin Ngigi"
__credits__ = None
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Kevin Ngigi"
__email__ = "kevinngigi110@gmail.com"
__status__ = "Prototype"


class Guess:
    def __init__(self, count, points):
        self.count = count
        self.points = points

    def play_game(self):
        answer = str('Lion')
        question = str('Who is the king of the Jungle?')

        while self.count != 0:
            print(f'{question}  You have {self.count} guesses to go:\n')
            user = str(input())

            if user == answer:
                print(f'correct! You have earned {self.points} points')
                return True
                # I have a problem with this line of code. Says This code is unreachable
                self.points = self.points + 5
            else:
                print('Incorrect! Try Again')
            self.count -= 1


if __name__ == '__main__':
    app = Guess(5, 0)
    while app.play_game() != True:
        break
    else:
        print('The End!')
