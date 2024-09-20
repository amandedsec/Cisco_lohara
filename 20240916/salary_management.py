def add_salary(salaries, salary):
    salaries.append(salary)

def remove_salary(salaries, salary):
    try:
        salaries.remove(salary)
    except ValueError:
        print('No such salary')

def sum_salaries(salaries):
    return sum(salaries)

def avg_salary(salaries):
    if len(salaries) == 0:
        return 0
    return sum(salaries) / len(salaries)

def max_salary(salaries):
    if len(salaries) == 0:
        return None
    return max(salaries)

def min_salary(salaries):
    if len(salaries) == 0:
        return None
    return min(salaries)

def menu():
    print('''1. Add Salary
2. Remove Salary
3. Sum of Salaries
4. Average of Salaries
5. Minimum Salary
6. Maximum Salary
7. End''')
    choice = int(input('Your choice: '))
    return choice

def main():
    salaries = []
    while True:
        choice = menu()
        if choice == 1:
            salary = float(input('Enter salary: '))
            add_salary(salaries, salary)
            print(salaries)
        elif choice == 2:
            salary = float(input('Enter salary: '))
            remove_salary(salaries, salary)
            print(salaries)
        elif choice == 3:
            print('Sum of salaries:', sum_salaries(salaries))
        elif choice == 4:
            print('Average salary:', avg_salary(salaries))
        elif choice == 5:
            min_sal = min_salary(salaries)
            if min_sal is not None:
                print('Minimum salary:', min_sal)
            else:
                print('No salaries available.')
        elif choice == 6:
            max_sal = max_salary(salaries)
            if max_sal is not None:
                print('Maximum salary:', max_sal)
            else:
                print('No salaries available.')
        elif choice == 7:
            print('App Ended')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()
