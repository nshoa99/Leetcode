def split(s, c):
    word = ""
    aList = []
    for letter in s:                # Lặp qua các chữ
        if letter == c:             # Nếu chữ này là khoảng trắng 
            if word != "":          # word không phải là rỗng
                aList.append(word)
            word = ""               # reset word  
        else:
            word += letter          # thêm những chữ đó vào
    
    if word != "":                  # thêm phần tử cuối cùng vào 
        aList.append(word)   
    return aList



print(split("    1asdasdasdasd asdadasd a 222 asdasd"," "))