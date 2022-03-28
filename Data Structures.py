#!/usr/bin/env python

from collections import deque

"""
This is my own implementation of Stacks, Queues and Linked Lists in Python.
In a stack, it is LIFO and Queues have FIFO 
"""

__author__ = "Kevin Ngigi"
__copyright__ = "Copyright (C) 2022 Kevin Ngigi"
__license__ = "Apache License 2.0"
__maintainer__ = "Kevin Ngigi"
__email__ = "kevinngigi110@gmail.com"
__status__ = "Prototype"


class Stack:
    #Using deque over lists gives faster append and pop operations
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return self.items == deque([])

    # The args help to insert a list or tuple into the queue
    def push(self, *item):
        self.items.insert(0, item)
    
    #Slight issues that need addressing on this function
    def pop(self):
        #print(f'You have popped {self.items(0)} from the stack')
        return self.items.pop()


    def view_stack(self):
        return f'{len(self.items)} items are available and they are:\n{self.items} '


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # The args help to insert a list or tuple into the queue
    def push(self, *item):
        print(f'You have inserted {item} into the Queue')
        return self.items.insert(0, item)
    
    def pop(self):
        print(f'{self.items.pop(0)} has been popped from the Queue')
        return self.items


    def view_queue(self):
        return f'{len(self.items)} items are available and they are:\n{self.items} '


if __name__ == '__main__':
    stack = Stack()
    queue = Queue()
    

