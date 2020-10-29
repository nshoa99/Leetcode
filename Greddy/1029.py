import collections
def twoCitySchedCost(costs):
    A = 0
    Diff = []
    for cost in costs:                      # O(n)
        A += cost[0]
        Diff.append(cost[1] - cost[0])
    
    Diff = sorted(Diff)                     # O(nlog(n))

    return A + sum(Diff[:len(costs) // 2])

# Time complexity O(nlog(n)), Extra space complexity O(n)

print(twoCitySchedCost(costs = [[10,20],[30,200],[400,50],[30,20]]))