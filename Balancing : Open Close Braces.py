###APPROAch

1) first create dictionary of braces closing:opening
2) iterate through string,
3) if the first character is a closing bracket then immediately we know its not balanced. so we check if the character is a closing bracket and that the stack is empty.
4) if its not , then we pop the top element off and check if its the equivalent opening bracket, if not then also false. 
5) otherwise if it was a opening bracket then just append. 




class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing brackets to their corresponding opening brackets
    
        for char in s:
            if char in braces_map: 
                if not stack:
                    return False

                top_element = stack.pop()
                if braces_map[char] != top_element:  
                    return False

            else: 
                stack.append(char)
        
        return not stack






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
