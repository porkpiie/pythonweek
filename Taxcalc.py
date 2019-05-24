name=input("Your Name?:")
salary=int(input("Your Wage before tax?:"))
if salary<3750:
    tax=salary/100*20
    ni=salary/100*12
else:
    tax=salary/100*40
    ni=salary/100*12
netsalary=salary-tax-ni
print("Name:", name)
print("Wage before tax:",salary)
print("Tax paid:", tax)
print("NI:", ni)
print("Take Home:",netsalary)
