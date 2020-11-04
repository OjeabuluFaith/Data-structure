'''
3rd of november 2020

implementing GRAPH using OOP

-->VERTEX
-->EDGES


'''
class AdjacentNode:
    def __init__(self,vertex):
        self.vertex = vertex 
        self.next = None
        
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices 
        self.graph = [None] * self.vertices
        
        
        
 