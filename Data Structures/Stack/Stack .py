from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
def reverse_string(string):
    stack=Stack()
    for char in string:
        stack.push(char)
    reversed_string=""
    while not stack.is_empty():
        reversed_string+=stack.pop()
    return reversed_string
def is_parentheses_balanced(string):
    stack = Stack()
    
    for char in string:
        if char in "([{":
            stack.push(char)

        elif char in ")]}":
            if stack.is_empty():
                return False
                
            # Check for a matching pair
            top = stack.peek()
            if (char == ")" and top == "(" or 
                char == "]" and top == "[" or 
                char == "}" and top == "{"):
                stack.pop()
            else:
                return False
    return stack.is_empty()

string="We will conquer HantaVirus"
reversed_string=reverse_string(string)
print(reversed_string)
balanced=is_parentheses_balanced("((()))")
print(balanced)