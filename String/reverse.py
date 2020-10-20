# Input = "abcd"
# Output = "dcba"

# def reverse(s):
#     return s[::-1]    # Bản chất là 1 vòng lặp, nhưng lặp theo chiều ngược 


def reverse(s):
    aSt = ''
    for i in range(len(s) - 1, -1 , -1):
        aSt += s[i]
    return aSt


def reverseUsingTwoPointers(s):
    i = 0
    j = len(s) - 1
    aList = list(s)    # convert to List, because of string is immutable
    while i <= j:
        aList[i], aList[j] = aList[j], aList[i]
        i += 1
        j -= 1
    return "".join(aList)



print(reverse("abcd"))
print(reverseUsingTwoPointers("abcd"))