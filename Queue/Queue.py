__header__ = "Queue"
"""
  " The Queue file consist of an QueueEmptyError class and Queue class with a inner Node class. The Queue class represents
  " a regular queue, with First In, First Out (FIFO) format. This is done using a linked list as the underlying data structure.
  " Consist of all the expected operations you would have for a Queue as well as a custom exception defined as StackEmptyError.
"""
__author__ = "Andy"
__since__ = "12/24/2021"
__purpose__ = "Future Reference and Practice"
# This class is a custom exception for when the program spots that the Queue is empty.
class QueueEmptyError(Exception):
    __module__ = Exception.__module__
    def __init__(self, message):
        super().__init__(message)
# This class represents that data structure known as the queue, with a front and rear pointers that allow
# for O(1) enqueuing and dequeuing. This class supports isEmpty, length, enqueue, dequeue, peek
# reversed, str and repr methods.
class Queue:
    # Inner class that represents a node, used as the data structure that represents the Queue.
    class Node:
        def __init__(self, item, next = None):
            self.item = item
            self.next = next
    
    def __init__(self, item = None):
        self.front = self.rear = self.Node(item)
        self.size = 1 if item else 0

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size
        
    # Enqueue method, enqueues the item to the back of the queue.
    def enqueue(self, item):
        node = self.Node(item)
        if self.front == None or self.front.item == None: 
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
        self.size += 1

    # Dequeue method, dequeues the item from the front of the queue.
    def dequeue(self):
        if hasattr(self.front, 'item'):
            front = self.front
            self.front = self.front.next
            self.size -= 1
            return front.item
        else:
            raise QueueEmptyError("Queue is Empty.")
            
    # Returns the front of the queue without dequeuing.
    def peek(self):
        if hasattr(self.front, 'item'):
            return self.front.item
        else:
            raise QueueEmptyError("Queue is Empty.")
    # Reverses the queue, note this is a linked list reversal versus a queue reversal.
    def reversed(self):
        curr, prev, after = self.front, None, None
        self.rear = self.front
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        self.front = prev

    # Details the representation of the queue in Python.
    def __repr__(self):
        if self.length() == 0:
            return f"{self.__class__.__name__}(front={None}, size={self.length()})"
        else:
            return f"{self.__class__.__name__}(front={self.peek()}, size={self.length()})"

    # Returns the string representation of the queue.
    def __str__(self):
        if self.length() == 0:
            return "[]"
        retStr, size = '[', self.length()
        while size > 1:
            retStr += f"{self.peek()}, "
            self.enqueue(self.dequeue())
            size -= 1
        retStr += f"{self.peek()}]"
        self.enqueue(self.dequeue())
        return retStr

            
    

    