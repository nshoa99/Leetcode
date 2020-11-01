class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0 
        aDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        i = 0
        while i < n- 1:
            if aDict[s[i]] >= aDict[s[i + 1]]:
                total += aDict[s[i]]
                i += 1
            else:
                total += aDict[s[i + 1]] - aDict[s[i]]
                i += 2
                
        if i == n - 1:
            total += aDict[s[i]]
            
        return total
           