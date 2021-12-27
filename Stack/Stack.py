__header__ = "Stack"
"""
  " The Stack file consist of an StackEmptyError class and Stack class with a inner Node class. The Stack class represents
  " a regular stack, with Last In, First Out (LIFO) format. This is done using a linked list of the underlying data structure.
  " Consist of all the expected operations you would have for a Stack as well as a custom exception defined as StackEmptyError.
"""
__author__ = "Andy"
__since__ = "12/19/2021"
__purpose__ = "Future Reference and Practice"
# This class is used to help define a user-defined exception (inheriting attributes from the Exception class).
class StackEmptyError(Exception):
    __module__ = Exception.__module__
    def __init__(self, message):
        super().__init__(message)
# This class represents the data structure known as the stack, consist of all the functions you would come to
# expect for a Stack such as pop, push, peek, str, and isEmpty.
class Stack:
    # Inner class that represents a node, used as the data structure that represents the stack
    class Node:
        def __init__(self, item, next = None):
            self.item = item
            self.next = next
    
    def __init__(self):
        self.stack = self.Node("")
        self.size = 0

    # Push operation, pushes the item to the top of the stack.
    def push(self, item):
        if self.length() == 0:
            self.stack.next = self.Node(item)
        else:
            new = self.Node(item, self.stack.next)
            self.stack.next = new
        self.size += 1

    # Pop operation, pops off the top of the stack and returns it.
    def pop(self):
        top = getattr(self.stack.next, 'item', None)
        afterTop = getattr(self.stack.next, 'next', None)
        if top or afterTop:
            self.stack.next = afterTop
            self.size -= 1
            return top
        else:
            raise StackEmptyError("Stack is Empty")

    # Peek operation, returns what the top of the stack is without removal
    def peek(self):
        top = getattr(self.stack.next, 'item', None)
        if top:
            return top
        else:
            raise StackEmptyError("Stack is Empty")

    def clear(self):
        self.stack.next = None

    def length(self):
        return self.size

    def isEmpty(self):
        return self.length() == 0

    def __repr__(self):
        if self.length() == 0:
            return f"{self.__class__.__name__}(top={None}, len={self.length()})"
        else:
            return f"{self.__class__.__name__}(top={self.peek()}, len={self.length()})"

    def __str__(self):
        if self.length() == 0:
            return "[]"
        aux = Stack()
        retStr = "["
        count = 1
        while self.length() > 1:
            if count % 6 == 0:
                retStr += "\n"
            aux.push(self.pop())
            retStr += f"{aux.peek()}, "
            count += 1
        aux.push(self.pop())
        retStr += f"{aux.peek()}]"
        while aux.length() > 0:
            self.push(aux.pop())
        return retStr
