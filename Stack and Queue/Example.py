
def checkValid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    return len(stack) == 0 

# Time complexity O(n), Extra space complexity O(n)

s = "(())()"
print(checkValid(s))


