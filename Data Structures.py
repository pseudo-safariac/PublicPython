#!/usr/bin/env python
from collections import deque
"""
This is my own implementation of Stacks and Queues in Python.
"""

__author__ = "Kevin Ngigi"
__copyright__ = "Copyright (C) 2022 Kevin Ngigi"
__license__ = "Apache License 2.0"
__maintainer__ = "Kevin Ngigi"
__email__ = "kevinngigi110@gmail.com"
__status__ = "Prototype"


class Stack:
    def __init__(self):
        self.items = dique()
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        self.items.pop(0)
    
    def view_stack(self):
        return f'{len(self.items)} items are available and they are:\n{self.items} '
        
class Queue:
    pass

app = Stack()
app.view_stack()

