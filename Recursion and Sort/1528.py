def restoreString(s, indices):
    result = '' * len(s)
    for i, c in enumerate(s):
        result[indices[i]] = c
    return "".join(result)
