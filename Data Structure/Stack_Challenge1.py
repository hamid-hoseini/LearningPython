"""
Write a function to determine whether a string of brackets is balanced
It should return True if balanced. 
[[({})]] is an example of balanced brackets. [({)})] is not balanced.
"""

def balanced_brackets(s):
        
    stack = []
    brackets = {'(':')','[':']','{':'}'}
    
    for char in s:
        
        if char in brackets.keys():
            
            stack.append(char)
            
        else:
            
            if len(stack) == 0 or brackets[stack.pop()] != char:
                return False
            
    return len(stack) == 0

string = '[[({})]]'
balanced_brackets(string)
# return True

string_2 = '[({)})]'
balanced_brackets(string_2)
# return False

string_3 = '][[({})]]'
balanced_brackets(string_3)
# return False
