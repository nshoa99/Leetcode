def deleteback(S,T):
    def delete(S):
        result = []
        for c in S:
            if c != "#":
                result.append(c)
            elif result:
                result.pop()
        return "".join(result)
    
    return delete(S) == delete(T)




print(deleteback("a##c","#a#c"))