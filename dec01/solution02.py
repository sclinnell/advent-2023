file1 = open('input.txt', 'r')
Lines = file1.readlines()
count = 0 
dict = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for line in Lines:
    dictcount = 1
    for digstr in dict:
        if line.find(digstr) != -1:
            loc = int(line.find(digstr))
            loc = loc+1
            line = line[:loc] + str(dictcount) + line[loc + 1:]
        dictcount += 1
    
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
    count+=1
    # if count > 80 and count < 90:
    #     print(str(count) + " " + numstr)
    sum += int(numstr)
print(count)
print(sum)

            
