file1 = open('input.txt', 'r')
Lines = file1.readlines()
sum = 0
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    first = -1
    
    last = -1
    for char in line:
        
        if char.isnumeric() == True and first == -1:
            first = int(char)
        elif char.isnumeric() == True and first != -1:
            last = int(char)
        
    if last == -1:
        numstr = str(first)+str(first)
    elif first != -1:
        numstr = str(first)+str(last)
    print(numstr)
    sum += int(numstr)
print(count)
print(sum)
