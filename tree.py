'''
Author: Faith Ojeabulu 
3rd of november 2020

implementing TREE using OOP



'''

# creating the root


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")

        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Trvaersal type" + str(traversal_type) + "is not supported.")
            return False


# traversal


# pre order --> root -->left subtree --> right subtree

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + ".")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# inorder -->left --> root  --> right

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal


# postorder --> left -->right     -->root

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
