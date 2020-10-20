'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
'''
# 2 pointers and sort

# def findLongestWord(s = "abpcpleeee", d = "apple"):
#     i, j = 0, 0 
#     word = ""
#     while i < len(s) and j < len(d):
#         if s[i] != d[j]:
#             i += 1
#         else:
#             word += s[i]
#             i += 1
#             j += 1
#     return word

# print(findLongestWord())

def check(s, word):
    i, j = 0, 0 
    while i < len(s) and j < len(word):
        if s[i] != word[j]:
            i += 1
        else:
            i += 1
            j += 1
    return j == len(word)
    
def findLongestWord(s, d):
    result = ""
    for word in d:
        if check(s, word):
            if len(word) > len(result) or len(word) == len(result) and word < result:
                result = word
    return result


print(findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]))



    



    



