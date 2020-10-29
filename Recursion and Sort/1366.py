from collections import defaultdict, OrderedDict
def rankTeams(votes):
    aDict = {}
    for c in votes[0]:
        aDict[c] = [0 for _ in range(len(votes[0]))] + [c]
    
    for vote in votes:
        for i, v in enumerate(vote):
            aDict[v][i] -= 1
    aDict = OrderedDict(sorted(aDict.items(), key=lambda  x: x[1]))
    return "".join(aDict)





print(rankTeams(["ABC","ACB","ABC","ACB","ACB"]))

    