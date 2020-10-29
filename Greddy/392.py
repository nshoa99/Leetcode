def isSubsequence(s, t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    
    i, j = 0, 0 
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i +=1
        j +=1
    return i == len(s)

print(isSubsequence(s = "abc", t = "ahbgdc"))