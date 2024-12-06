import pandas as pd

file = 'day1'

list1 = []
list2 = []
count = 1
with open(file, 'r') as day1file:
    content =  day1file.read()
    # count += 1
    for line in content.strip().split("\n"):
        count += 1
        values = line.split()
        list1.append(int(values[0]))
        list2.append(int(values[1]))
        # print(f"{line} {count}")
    

# print(list2)

list1.sort()
list2.sort()

totalDistance = 0
print(list1[1])

i = 0
for i,j in zip(list1, list2):
        # print(i)
        value = abs(i - j)
        print(value)
        totalDistance += value
        # i += 1

print(totalDistance)

# part 2 
finalising = 0

for value in list1:
    counting = 0
    for checkingValues in list2:
         if checkingValues == value:
              counting += 1
    temp = value * counting
    finalising += temp

print(finalising)




