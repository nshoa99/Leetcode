def reverseVowels(s):
    i = 0 
    j = len(s) - 1
    aList = list(s)
    vowels = {'u', 'e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I'}

    while i <= j:
        if not aList[i] in vowels:
            i += 1
        elif  not aList[j] in vowels:
            j -= 1
        else:
            aList[i], aList[j] = aList[j], aList[i]
            i += 1
            j -= 1
    return "".join(aList)
            


print(reverseVowels("leetcode"))