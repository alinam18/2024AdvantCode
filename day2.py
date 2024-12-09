# import pandas as pd

# file = 'day2'


# safeCount = 0
# count = 0
# rowCounting = 0

# newList  = []
# with open(file, 'r') as day2file:
#     content = day2file.read()
#     print('hi')
#     for line in content.strip().split('\n'):
#         rowCounting +=1
#         counting = 0
#         values = line.split()
#         # count = values[0]
#         valuesLength = len(values)
#         # print(values)
#         pre = 0
#         if values[0] < values[1]:
#             # print(f'{rowCounting} - increasing v')
#             # increasing
#             for currentNumbers in values:
#                 counting += 1
#                 # print(currentNumbers)
#                 if int(currentNumbers) <= int(pre) and currentNumbers != values[0]:
#                     # not safe
#                     # print(f'not safe pre = {pre} current = {currentNumbers} ')
#                     break
#                 elif counting == valuesLength and currentNumbers == values[valuesLength - 1] and currentNumbers > pre:
#                     safeCount +=1
#                     newList.append(line)
#                     print(f"{rowCounting} row is safe {line} - increasing")
#                     break
#                 pre = currentNumbers
#         elif values[0] > values[1]:
#             # decreasing
#             # print(f'{rowCounting} - decreasing')

#             for currentNumbers in values:
#                 counting += 1

#                 if int(currentNumbers) >= int(pre) and currentNumbers != values[0]:
#                     # not safe
#                     break
#                 elif counting == valuesLength and currentNumbers == values[valuesLength - 1] and currentNumbers < pre:
#                     safeCount +=1
#                     newList.append(line)
#                     print(f"{rowCounting} row is safe {line} - decreasing")

#                     break
#                 pre = currentNumbers

#         # if rowCounting == 5:
#             # break

# print(f"safe count {safeCount}")

# safe = 0
# safe = 0  # Initialize safe
# safeCountingFinal = 0
# for line in newList:
#     safe = 1 
#     values = list(map(int, line.split()))  # Convert all elements to integers
#     length = len(values)
#     for count in range(length - 1):  
#         if abs(values[count] - values[count + 1]) <= 3: 
#             safe += 1  
#             print(f"{safe}  {length} - {line} || {values[count]} || {values[count + 1]} || {abs(values[count] - values[count + 1])}")
#         if safe == length:
#             safeCountingFinal += 1


#     # print(f'{line} -  {length}')
# print(safeCountingFinal)

# # print(newList)


# Initialize safe count
safeCount = 0
newList = []

file = 'day2'

with open(file, 'r') as day2file:
    content = day2file.read()
    
    for rowCounting, line in enumerate(content.strip().split('\n'), start=1):
        values = list(map(int, line.split()))  # Convert the string values to integers
        
        is_increasing = all(values[i] < values[i + 1] for i in range(len(values) - 1))
        is_decreasing = all(values[i] > values[i + 1] for i in range(len(values) - 1))

        valid_differences = all(1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))

        if (is_increasing or is_decreasing) and valid_differences:
            safeCount += 1
            newList.append(line)  
            print(f"Row {rowCounting} is safe: {line}")

print(f"Total safe count: {safeCount}")
