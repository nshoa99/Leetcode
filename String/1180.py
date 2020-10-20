def countSubstring(s):
    count = 0
    final = 0 
    aList = []
    for i in range(len(s)):
        if aList == []:
            aList.append(s[i])
            count = 1
        else:
            if s[i] == aList[-1]:
                count += 1
            else:
                aList.pop()
                final = count*(count + 1) // 2
                aList.append(s[i])
                count = 1
    return final + count*(count + 1) // 2


print(countSubstring("aaaaaaaaaa"))

