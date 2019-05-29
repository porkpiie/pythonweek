def tax(Salary):
    if Salary>3750:
        t=Salary/100*30
    else:
        t=Salary/100*20
    return t


Salary = int(input("Enter your salary: "))

print ("Your tax: ", tax(Salary))
print ("Net: ",(Salary - tax(Salary)))