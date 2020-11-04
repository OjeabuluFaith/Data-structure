'''
3rd of november 2020

implementing SINGLY LINKED LIST  using OOP

-->create node
-->create linkedlist 
-->add node to linkedlist 
-->print linkedlist 

'''

# creating the nodes


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # since the pointer does not point to anything initially 


class LinkedList:
    def __init__(self):
        self.head = None   # head node... starting point

# inserting an element

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            
            lastNode  = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode == lastNode.next
            lastNode.next = newNode 
            
    def printList(self ):
        
        currentNode 
                 

# adding/inserting element into the linkedlist
