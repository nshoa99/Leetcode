import collections
def carFleet(target, position, speed):
    cars = collections.defaultdict(list)

    for i, p in enumerate(position):
        cars[p] = speed[i]
    cars = sorted(cars.items(), key= lambda x: -x[0])
    
    last_time = 0
    carFleet = 0

    for i in range(len(cars)):
        time = (target - cars[i][0]) / cars[i][1]
        if time > last_time:
            carFleet += 1
            last_time = time
    
    return carFleet

    

print(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))