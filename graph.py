'''
3rd of november 2020

implementing GRAPH using OOP

-->VERTEX
-->EDGES


'''
graph = {"A": ["B", "C"],
         "B": ["D", "E", "A"],
         "C": ["A"],
         "D": ["B", "E"],
         "E": ["B", "D"]
         }

#creating a class graph

class Graph(object):
    def __init__(self, graph=None):
        if graph == None:
            graph = {}
            self.__graph = graph

#creating a node

    def add_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph:
            self.__graph[node1].append(node2)
        else:
            self.__graph[node1] = [node2]

    def nodes(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if (neighbour, node) not in edges:
                    edges.append((node, neighbour))
        return edges
    
    
#he __str __ () method that will allow you to display the graph, passing it directly as an argument in the print() function.

    def __str__(self):
        res = "nodes: "
        for node in self.nodes():
            res += str(node) + " "
            res += "\nedges: "
        for edge in self.edges():
            res += str(edge) + " "
        return res
