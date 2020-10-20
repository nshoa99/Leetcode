class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = dict()
        for i in range(len(S)):
            last[S[i]] = i
        
        finals = []
        j, k = 0, 0
        for i in range(len(S)):
            k = max(k, last[S[i]])
            if i == k:
                s = k - j + 1
                finals.append(s)
                j = k + 1
        return finals
	    

        