'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''

    
def wordPattern(pattern, s):
    sList = list(s.split())
    a = len(set(pattern))
    b = len(set(sList))

    return len(pattern) == len(sList) and a == b and a == len(set(zip(pattern,sList)))


print(wordPattern("abba", "sy hoa hoa sy"))  





