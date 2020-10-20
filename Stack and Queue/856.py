'''
SCORE OF PARENTHESES

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50

'''

def scoreOfParentheses(S):
    stack = [0]
    for c in S:
        if c == '(':
            stack.append(0)
        else:
            last = stack.pop()
            stack[-1] += 1 if last == 0 else 2*last
    return stack.pop()

# Time complexity O(n), Extra space complexity O(n)

print(scoreOfParentheses("((())())"))