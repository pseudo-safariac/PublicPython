#!/usr/bin/env python

from collections import deque

"""
This is my own implementation of Stacks, Queues and Linked Lists in Python.
In a stack, it is LIFO and Queues have FIFO .
Attributes are:
    is_empty
    push
    pop
    view_stack
    view_queue
Methods are:
    self.items : list
    
"""

__author__ = "Kevin Ngigi"
__copyright__ = "Copyright (C) 2022 Kevin Ngigi"
__license__ = "Apache License 2.0"
__maintainer__ = "Kevin Ngigi"
__email__ = "kevinngigi110@gmail.com"
__status__ = "Prototype"


class Stack:
    def __init__(self):
        # Using deque over lists gives faster append and pop operations
        self.items = deque()

    def __str__(self):
        return f'{self.items}'

    def __repr__(self):
        return f'{self.items}'

    def is_empty(self):
        return self.items == deque([])

    def push(self, *item):
        # The args help to insert a list or tuple into the queue
        # print(f'You have pushed {item} to the stack')
        self.items.insert(0, item)

    def pop(self):
        return self.items.popleft()

    def view_stack(self):
        return f'{len(self.items)} items are available and they are:\n{self.items} '


class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return f'{self.items}'

    def __repr__(self):
        return f'{self.items}'

    def is_empty(self):
        return self.items == []

    def push(self, *item):
        # The args help to insert a list or tuple into the queue
        # print(f'You have inserted {item} into the Queue')
        return self.items.insert(0, item)

    def pop(self):
        # print(f'{self.items.pop(0)} has been popped from the Queue')
        return self.items

    def view_queue(self):
        return f'{len(self.items)} items are available and they are:\n{self.items} '


if __name__ == '__main__':
    stack = Stack()
    queue = Queue()
    
