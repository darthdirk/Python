lst = []
print("Enter 5 numbers: ")
# loop x5
for x in range(5):
    lst.append(eval(input()))
    # float from user
maxVal = lst[0]
minVal = lst[0]
total = 0
avg = 0
# total ave max min
for y in lst:
    if(maxVal < y):
        maxVal = y
    if(minVal > y):
        minVal = y
    total += y
#intrest
print("Maximum =",maxVal)
print("Miniimum =",minVal)
print("Total =",total)
print("Average =",(total/5))
print("Interest: ")
print("-----------")
for z in lst:
    print(z + z * 0.2)
#  Thanks,
# Greg 
