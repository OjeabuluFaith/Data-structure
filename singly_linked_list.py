'''
3rd of november 2020

implementing SINGLY LINKED LIST  using OOP

-->access an el
-->add element
-->remove element
-->transerve


"""traversing operation 
-->start with the head
-->access the data if head is not empty 
-->goto next node access node data 
-->continue until the last node


'''

# creating the nodes


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # storing the pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # head node... starting point

# printing the information of each node

    def print_LL(self):
        if self.head == None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print (n.data)
                n = n.next 
                
#adding/inserting element into the linkedlist 

