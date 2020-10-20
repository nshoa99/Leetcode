def isLongPressedName(name, typed):
    if len(set(name)) != len(set(typed)):
        return False
    else:
        for c in set(name):
            if name.count(c) > typed.count(c):
                return False


    


print(isLongPressedName("syhoa","syhoa"))
    
 