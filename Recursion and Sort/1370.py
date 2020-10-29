# 1. Tính số lần xuất hiện của 1 ký tự trong chuỗi s
# 2. Lặp qua tất cả các ký tự từ 'a' -> 'z' và từ 'z' -> 'a', với điều kiện dừng là: len(result) > len(s)
# 3. Nếu số lần xuất hiện của 1 ký tự khác 1 
# 3.1 Thêm vào result
# 3.2 Số lần xuất hiện của ký tự đó - 1

import collections
import string

def sortString(s):
    cnt = collections.Counter(s)
    result = []
    alphabet = string.ascii_lowercase
    r_alphabet = sorted(alphabet, reverse=True)
    
    while len(result) < len(s):
        for c in alphabet:
            if cnt[c] != 0:
                result.append(c)
                cnt[c] -= 1
        for c in r_alphabet:
            if cnt[c] != 0:
                result.append(c)
                cnt[c] -= 1
    return "".join(result)

print(len(sortString("aaaabbbbccc")))

# sortString("aaabbbccc")


