def find_quotient(d, n):
    if n == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return d / n

try:
    number = int(input("Enter a number: "))
    result = find_quotient(10, number)  # 10 / number
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError as e:
    print(e)
else:
    print(f"The result is: {result}")
finally:
    print('Cleaning up...')
print('End of program')
