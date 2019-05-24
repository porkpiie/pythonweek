name=input("Your Name?:")
salary=int(input("Your Wage before tax?:"))
if salary<3750:
    tax=salary/100*20
else:
    tax=salary/100*40
netsalary=salary-tax
print("Name:", name)
print("Wage before tax:",salary)
print("Tax paid:", tax)
print("Take Home:",netsalary)
