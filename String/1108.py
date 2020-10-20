''' 
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

'''

# def IPv4(address):
#     new_adress = address.split('.')
#     aList = []
#     for i in range(len(new_adress)):
#         aList.append(new_adress[i])
#         aList.append('[.]')
#     aList.pop(-1)
#     return "".join(aList)


def IPv4(address):
    aList = []
    for c in address:
        if c != '.':
            aList.append(c)
        else:
            aList.append('[.]')
    return "".join(aList)



print(IPv4("255.255.0.254"))