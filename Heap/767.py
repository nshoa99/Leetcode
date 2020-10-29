import heapq
import collections

class Entry:
    def __init__(self, val, cnt):
        self.val = val
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt > other.cnt
    
    def __repr__(self):
        return "{}-{}".format(self.val, self.cnt)
    
class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = collections.Counter(S)
        items = list(cnt.items())
        for i in range(len(items)):
            val, cnt = items[i]
            items[i] = Entry(val, cnt)
        
        heapq.heapify(items)
        
        new_string = ""
        while len(items) >= 2:
            # Lấy 2 phần tử đầu tiên ra
            item1 = heapq.heappop(items)
            val1, cnt1 = item1.val, item1.cnt
            item2 = heapq.heappop(items)
            val2, cnt2 = item2.val, item2.cnt
            
            new_string += "{}{}".format(val1, val2) * cnt2
            cnt1 -= cnt2
            
            if cnt1 > 0:
                heapq.heappush(items, Entry(val1, cnt1))
                
        if len(items) == 1:
            item = heapq.heappop(items)
            if item.cnt != 1:
                return ""
            else:
                new_string += item.val
        return new_string
        
