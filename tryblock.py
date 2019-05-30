try:
    no1=int(input("Enter first integer: "))
    no2=int(input("Enter second integer: "))
    result = no1/no2
    print("Result is", result)

except ValueError:
    print("Please enter only numbers: ")

except ZeroDivisionError:
    print("What are you doing? Don't divide by zero")

except Exception:
    print("Failed to execute, please try again")

finally:
    print("Finished.")