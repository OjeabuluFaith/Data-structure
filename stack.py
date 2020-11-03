'''
2nd of november 2020

implementing STACK using OOP

-->POP METHOD 
-->PUSH METHOD
-->PEEK
-->SIZE
-->EMPTY(to check if the stack is empty or not)

using the LIFO implemenetation'''


class Stack(object):

    def __init__(self):
        self.item = []

   # putting a new element on the stack

    def push(self, item = ''):

        self.item.append(item)
        pass

   # removing an element from the stack

    def pop(self):

        self.item.pop()
        pass

    # checking if an element is present in the stack

    def peek(self):

        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):

        if self.item:
            return len(self.item)
        else:
            return None

# checking if the stack is empty or not

    def isempty(self):
        if self.item == []:
            return True
        else:
            return False
        

if __name__ == "__main__":
    stack = Stack()
    
    stack.push("1")
    stack.push("2")
    print(stack.size())
    print(stack.peek())
    
    
    
    
    stack.pop()
    print(stack.size())
    print(stack.peek())
    
    print(stack.isempty())