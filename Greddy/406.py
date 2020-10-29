def reconstructQueue(people):
    people = sorted(people, key=lambda x: (-x[0], x[1]))
    result = []
    for p in people:
        result.insert(p[1], p)
    return people


print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))