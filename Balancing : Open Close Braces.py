def is_balanced_braces(string):
    stack = []
    braces_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing brackets to their corresponding opening brackets
    
    for char in string:
        if char in braces_map.values():
            stack.append(char)  # Push opening brackets onto the stack
        elif char in braces_map:
            if not stack or stack.pop() != braces_map[char]:
                return 'No'
    
    if not stack:
        return 'Yes'  # If the stack is empty, return 'Yes' indicating balanced braces
    else:
        return 'No'   # If the stack is not empty, return 'No' indicating unbalanced braces

def verify_braces_balance(braces):
    return [is_balanced_braces(string) for string in braces]

# Test the function with the example input
braces = ['[{}]', '[{]}']
print(verify_braces_balance(braces))  # Output: ['Yes', 'No']





Q.
python question

open and closed tickets are represented by different open and closed braces respectively. for example each of the braces '([{ represent an open ticket and need matching braces')]}' in that order to close them

braces in a string are balanced if the following conditions are met:
all open braces must be closed
each closed brace must have a matching open brace
any set of nested braces must be closed before its surrounding brace

given an 2-dimensional array of strings compriced of braces, verify that the braces in each string are balanced.
return 'Yes' if the braces and 'No' otherwsie. 

for example

braces = ['[{}]','[{]}']

the braces in the first string are balanced because all braces are closed and all nested braces are closed in order
the braces in the second string are not balanced because the nested brace '{' was not closed before its surroiunding '[]' , so th eorder was not respected
the result is ['Yes', 'No']
