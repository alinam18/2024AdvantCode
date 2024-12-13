import re 
safeCount = 0
newList = []

file = 'day3'

pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
number = r'[0-9]{1,3}'

# part 1
with open(file, 'r') as day3file:
    content = day3file.read()
    
    re.search(pattern, content)

    yay  = re.findall(pattern, content)
    overallnumber = 0
    for value in yay:
        print(value)
        xman = re.findall(number, value)
        print(xman)
        if xman:
            num1 = int(xman[0])  # First number
            num2 = int(xman[1])  # Second number
            number_result = num1 * num2  #
            overallnumber += number_result

    print(overallnumber)

# part 2

splitingPatterns = r"don't\(\)|do\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)"
with open(file, 'r') as day3file:
    content = day3file.read()
    
    splitingaway  = re.findall(splitingPatterns, content)
    current = 0
    overallnumber = 0
    for value in splitingaway:
        print(value)
        if value == "don't()":
            current = 1
            continue
        if value == "do()":
            current = 0
            continue
        
        if current == 0:
            xman = re.findall(number, value)
            # print(xman)
            if xman:
                num1 = int(xman[0])  
                num2 = int(xman[1])  
                number_result = num1 * num2  
                overallnumber += number_result

# 19021239
print(overallnumber)