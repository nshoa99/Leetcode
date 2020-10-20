def isPalindrome(string):
    i = 0 
    middle = len(string) // 2

    while i < middle:
        j = len(string) - 1 - i 
        if string[i] != string[j]:
            return False
        i += 1
    return True


print(isPalindrome("asd2bdsa"))

### time complexity O(N)
### i and j: 2 pointers