def minAddtoMakeValid(S):
    stack = []

    for c in S:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
    
    return len(stack)



    


print(minAddtoMakeValid("())"))