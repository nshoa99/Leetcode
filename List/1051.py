import collections

def heightChecker(heights):
    count = collections.Counter(heights)
    print(count)
    
    i, result = 1, 0 
    for h in heights:
        while count[i] == 0:
            i += 1
        if i != h:
            result += 1
        count[i] -= 1
    return result

print(heightChecker([1,1,4,2,1,3]))