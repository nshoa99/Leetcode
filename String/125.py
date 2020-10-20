def isPalindrome(s):
    i = 0
    j = len(s) - 1

    while i <= j:
        if not s[i].lower().isalnum():
            i += 1
        elif not s[j].lower().isalnum():
            j -= 1
        else:
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
    
    return True 



print(isPalindrome("race a car"))
print(isPalindrome("syhoa aohys"))

# 0(1) Extra Space
# O(N) Time complexity
            