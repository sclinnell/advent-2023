file1 = open('input.txt', 'r')
Lines = file1.readlines()
count = 0 
dict = ["1","2","3","4","5","6","7","8","9","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
edge_cases = ["oneight","twone","threeight","fiveight","sevenine","eightwo","eighthree","nineight"]
solutions = ["oneeight","twoone","threeeight","fiveeight","sevennine","eighttwo","eightthree","nineeight"]

sum = 0
for line in Lines:
    edge_counter = 0
    for case in edge_cases:
        line = line.replace(case, solutions[0])
        edge_counter += 1
    temp = ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
    counter = 0 
    dictcount = 1
    newstr = ''
    for digstr in dict:
        loc = line.find(digstr)
        tempstr = line
        while loc != -1:
            if(counter < 9):
                temp[loc] = digstr
            else:
                temp[loc] = str(dictcount)
            print(digstr+str(loc))

           
            tempstr = tempstr.replace(digstr,'x',1)
            print(tempstr)
            loc = tempstr.find(digstr)
            print(str(loc))

        if counter >= 9:        
            dictcount += 1
        counter += 1
    new = list(filter(('x').__ne__, temp)) 
    numstr = new[0]+new[-1]
    


    
#     first = -1
#     last = -1
#     for char in line:
        
#         if char.isnumeric() == True and first == -1:
#             first = int(char)
#         elif char.isnumeric() == True and first != -1:
#             last = int(char)
        
#     if last == -1:
#         numstr = str(first)+str(first)
#     elif first != -1:
#         numstr = str(first)+str(last)
    count+=1
    print(line+str(count) + " " + numstr)
    print(new)
    sum += int(numstr)
print(count)
print(sum)
   

print(count)
            
