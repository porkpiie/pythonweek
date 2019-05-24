Price = input("Enter price of product: £")
Money = input("Enter amount of cash given: £")
Change = (int(Money)-int(Price))
print("Change due is: £",Change)
print("----------------")
Fifty=Change // 50
Twenty=Change % 50 // 20
Ten=Change % 50 % 20 // 10
Five=Change % 50 % 20 % 10 // 5
Two=Change % 50 % 20 % 10 % 5 // 2
One=Change % 50 % 20 % 10 % 5 % 2 // 1

if Fifty>0:
    print("£50 notes= ",Fifty)
if Twenty>0:
    print("£20 notes= ",Twenty)
if Ten>0:
    print("£10 notes= ",Ten)
if Five>0:
    print("£5 notes= ",Five)
if Two>0:
    print("£2 coins= ",Two)
if One>0:
    print("£1 notes= ",One)