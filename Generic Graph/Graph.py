__header__ = "Graph"
#  The Graph class consist of a Adjacency Node class that forms a linked list for every vertex present on the
#  graph. The linked list represents the edges and possible weights to the graph. It supports adding, getting,
#  and printing if weight is supported or not. The Adjacency Node class consist of getters, and a iter so that
#  the linked list can be traversed if required.
__author__ = "Andy"
__since__ = "12/20/2021"
__purpose__ = "Future Reference and Practice"
class Graph:
    # The AdjNode class supports basic linked list operations and each node has the ability
    # to hold a weight and a vertex.
    class AdjNode:
        def __init__(self, vertex, weight = 0, next = None):
            self._vertex = vertex
            self._weight = weight
            self.next = None

        @property
        def vertex(self):
            return self._vertex

        @property
        def weight(self):
            return self._weight
        
        def __str__(self):
            return f"{self.vertex}: {self.weight}"

        def __iter__(self):
            curr = self
            while curr:
                yield curr
                curr = curr.next

    def __init__(self, enableWeight = False):
        self.graph = {}
        self.enableWeight = enableWeight
        self.size = 0

    # The __setitem__ is a data model method that allows for vertices and their edges to be 
    # directly assigned and added to the graph.
    def __setitem__(self, fromVertex, toVertex):
        if isinstance(toVertex, tuple): toVertex, weight = toVertex
        else: toVertex, weight = toVertex, 0
        node = self.AdjNode(toVertex, weight)
        if fromVertex in self.graph:
            node.next = self.graph[fromVertex]
            self.graph[fromVertex] = node
        else:
            self.graph[fromVertex] = node
            self.size += 1
        node = self.AdjNode(fromVertex, weight)
        if toVertex in self.graph:
            node.next = self.graph[toVertex]
            self.graph[toVertex] = node
        else:
            self.graph[toVertex] = node
            self.size += 1

    # The __getitem__ method is a data model method that allows for direct indexing to access
    # vertices within the graph.
    def __getitem__(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            raise Exception("Vertex not present in graph.")
    
    def __len__(self):
        return self.size

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self.size})"

    # Prints the graph and their edge's weights if the weight is a tagged option.
    def print_weighted(self):
        retStr = "Graph [Weighted] {\n"
        for vertex in self.graph:
            retStr += f"  {vertex}: ["
            curr = self.graph[vertex]
            while curr.next:
                retStr += f"{curr.vertex}: {curr.weight}, "
                curr = curr.next
            retStr += f"{curr.vertex}: {curr.weight}]\n"
        return retStr + '}'

    # Prints the graph but not their edge's weights if the weight is a untagged option.
    def print_unweighted(self):
        retStr = "Graph [Unweighted] {\n"
        for vertex in self.graph:
            retStr += f"  {vertex}: ["
            curr = self.graph[vertex]
            while curr.next:
                retStr += f"{curr.vertex}, "
                curr = curr.next
            retStr += f"{curr.vertex}]\n"
        return retStr + '}'

    def __str__(self):
        if self.size == 0: 
            return "[]"
        if self.enableWeight:
            return self.print_weighted()
        else:
            return self.print_unweighted()