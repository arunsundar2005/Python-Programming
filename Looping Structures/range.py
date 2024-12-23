print(range(0,10)) # Output -> range(0,10)
print(list(range(0,10)))# output -> [0,1,2,3,4,5,6,7,8,9]

print(list(range(0,10,2)))# output -> [0,2,4,6,8], the 2 represents the step, i.e what should be added to get the new number (current number)
                          # by default step is 1



for i in range(0,10):
    print(i)
    if i == 8:
        continue
    elif i==9:
        break
    else:
        print(i)
    
