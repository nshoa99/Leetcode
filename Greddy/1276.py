'''
Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 Tomato slices and 1 cheese slice.
Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

 

Example 1:

Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.
Example 2:

Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
Explantion: There will be no way to use all ingredients to make small and jumbo burgers.
Example 3:

Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
Example 4:

Input: tomatoSlices = 0, cheeseSlices = 0
Output: [0,0]
Example 5:

Input: tomatoSlices = 2, cheeseSlices = 1
Output: [0,1]
'''

# Using math to solve the problem

# def numOfBurgers(tomatoSlices, cheeseSlices):
#     x, y = 0, 0 
#     # x = numOfJumbo and y = numOfSmall
#     x = (tomatoSlices - 2 * cheeseSlices) / 2
#     y = cheeseSlices - x

#     return [int(x),int(y)] if x >= 0 and y >= 0 else []


# Greedy

# def numOfBurgers(tomatoSlices, cheeseSlices):
#     # x = numOfJumbo 
#     # y = numOfSmall
#     x, y = 0, 0
#     for x in range(0, cheeseSlices + 1):
#         y = cheeseSlices - x
#         if 4*x + 2*y == tomatoSlices:
#             return [x, y]
#     return []
# Time limit exceeded -> imporving by using Binary Search 

# i, j = 0, cheeseSlices
# middle = i + j // 2
# Lặp vòng while i <= j:
#   -> Trong vòng lặp, tính x = (i + j) // 2, y = cheeseSlices - x
#   -> Nếu 4*x + 2*y > tomatoSlices:
#       -> j = x - 1
#   -> Nếu 4*x + 2*y < tomatoSlices:
#       -> i = x + 1
#   -> return [x, y]


def numOfBurgers(tomatoSlices, cheeseSlices):

    i = 0
    j = cheeseSlices
    while i <= j:
        x = (i + j) // 2
        y = cheeseSlices - x
        if 4 * x + 2 * y > tomatoSlices:
            j = x - 1
        elif 4 * x + 2 * y < tomatoSlices:
            i = x + 1
        else:
            return [x, y]
    return []
         



print(numOfBurgers(16, 7))