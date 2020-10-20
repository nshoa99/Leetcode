''' 
Find the longest subtring without repeating characters
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
''' 


def lengthOfLongestSubString(s):
    n = len(s)
    cur_chars = set()
    i, j = 0, 0
    max_len = 0 

    while i < n and j < n:
        if s[j] not in cur_chars:
            cur_chars.add(s[j])
            j +=1
            max_len = max(max_len, j - i)
        else:
            i +=1
            cur_chars.remove(s[i])
    
    return max_len


print(lengthOfLongestSubString("abcabcbb"))





