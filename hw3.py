arr = []
for x in range(5):
    number1 = input('Enter the Number \n')
    arr.append(int(number1))

minNum = arr[0]
maxNum = 0

for item in arr:
    if item < minNum:
        minNum = item
    elif item > maxNum:
        maxNum = item

print(minNum, maxNum)
