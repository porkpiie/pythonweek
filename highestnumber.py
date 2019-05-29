numbers=[]


while True:
    num=int(input("Enter any integer: "))
    if num == 0:
        break
    else:
        numbers.append(num)


highest=numbers[0]
i=1
while i<len(numbers):
    if numbers[i]>highest:
        highest=numbers[i]
    i+=1


print("Highest number in list is: ", highest)