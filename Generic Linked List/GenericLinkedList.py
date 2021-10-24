__header__ = "Generic Linked List"
#  The Generic Linked List class consist of a Generic Node that form a linked list that allows for
#  adding, removing, printing, searching, and sorting the list. The Generic Node class consist of a 
#  simple initializer, getters and setters for the given node.
__author__ = "Andy"
__since__ = "10/23/2021"
__purpose__ = "Future Reference and Practice"
class GenericLinkedList:
    __header__ = "Generic Node"
    # The following class represents the node, its attributes, and methods for getting and setting
    # those attributes.
    class GenericNode:
        def __init__(self, data, next = None) -> None:
            self.data = data
            self.next = next
        def get_data(self):
            return self.data
        def set_data(self, data):
            self.data = data
        def get_next(self):
            return self.next
        def set_next(self, next):
            self.next = next
    def __init__(self, data = None, node = None) -> None:
        if data is None and node is None:
            self.head = None
            self.size = 0
        else:
            if node is None:
                self.head = GenericLinkedList.GenericNode(data)
            else:
                self.head = node
            self.size = 1
    def get_size(self) -> int:
        return self.size
    def reset_head(self) -> None:
        self.head = None
    # The add_node() function takes in arguments to add an element at the
    # end of the list. Or to add at a position in the linked list.
    def add_node(self, data, position = -1) -> None:
        if self.head is None:
            self.head = GenericLinkedList.GenericNode(data)
        else:
            curr = self.head
            if position > 0 and position <= self.size:
                for _ in range(1, position - 1):
                    curr = curr.next
                next = curr.next
                curr.next = GenericLinkedList.GenericNode(data)
                curr.next.next = next
            else:
                while curr.next != None:
                    curr = curr.next
                curr.next = GenericLinkedList.GenericNode(data)
        self.size += 1
    # The remove_node() function takes in an index and removes the
    # element in the linked list at the position. Returns true if the
    # removal is done else false if not.
    def remove_node(self, index = -1) -> bool:
        if self.head is None: return False
        else:
            if index < 0 or index > self.size:
                return False
            self.size -= 1
            if index == 1:
                self.head = self.head.next
                return True
            curr = self.head
            for _ in range(1, index - 1):
                curr = curr.next
            parent = curr
            parent.next = curr.next.next
            return True
    # Performs a linear search in the linked list, has options to search
    # for the first occurrence of the target or search for a target at a
    # specific position using default arguments. Returns true if its found
    # else false if its not. 
    def find_node(self, target = None, index = -1) -> bool:
        if self.head is None: return False
        if target is not None:
            curr = self.head
            if index > 0 and self.size >= index:
                for _ in range(1, index):
                    curr = curr.next
                if curr.data == target:
                    return True
            else:
                while curr != None:
                    if curr.data == target:
                        return True
                    curr = curr.next
            return False
    # The print() function prints the linked list and returns it in string
    # format.
    def print(self) -> str:
        curr = self.head
        ret = "["
        if curr == None:
            return ret + "]"
        newLine = 1
        while curr.next != None:
            if newLine % 10 == 0: ret += "\n"
            ret += f'{curr.data}, '
            curr = curr.next
            newLine += 1
        return ret + f'{curr.data}]'
    # The reverse() function reverses the linked list. Does this in a single
    # pass using three pointers.
    def reverse(self) -> None:
        curr = self.head
        prev = next = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    # The merge_sort() function sorts the given linked list in ascending
    # format. Mergesort performs a divide and conquer strategy to sort the given
    # linked list. It uses internal helper functions to perform this.
    def merge_sort(self) -> None:
        def frontBackSplit(source):
            # if the length is less than 2, handle it separately
            if source is None or source.next is None:
                return source, None
            (slow, fast) = (source, source.next)
            # advance `fast` two nodes, and advance `slow` one node
            while fast:
                fast = fast.next
                if fast:
                    slow = slow.next
                    fast = fast.next
            # `slow` is before the midpoint of the list, so split it in two
            # at that point.
            ret = (source, slow.next)
            slow.next = None
            return ret
        # Takes two lists sorted in increasing order and merge their nodes
        # to make one big sorted list, which is returned
        def sortedMerge(left, right):
            # base cases
            if left is None: return right
            elif right is None: return left
            # pick either `a` or `b`, and recur
            if left.data <= right.data:
                result = left
                result.next = sortedMerge(left.next, right)
            else:
                result = right
                result.next = sortedMerge(left, right.next)
            return result
        def sorting(node):
            # base case — length 0 or 1
            if node is None or node.next is None:
                return node
            # split `head` into `a` and `b` sublists
            front, back = frontBackSplit(node)
            # recursively sort the sublists
            front = sorting(front)
            back = sorting(back)
            # answer = merge the two sorted lists
            return sortedMerge(front, back)
        self.head = sorting(self.head)
    # Saves the input from the user into a file
    def save_to_file(self, filename) -> None:
        fout = open(filename, "w")
        fout.write(self.print())
        fout.close()
    # Loads the data from a file, must be formatted like this:
    # [1, 2, yes, ok, 3412, 2.0, true]
    def load_from_file(self, filename) -> None:
        with open(filename, "r") as fin:
            for line in fin:
                elements = line.translate(str.maketrans({'[': '', ',': '', ']': '', '\n': None})).split(" ")
                for ele in elements:
                    if ele != '':
                        self.add_node(ele)


