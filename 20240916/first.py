class Employee:
    def __init__(self, name, address , code, salary):
        self.name = name
        self.address = address
        self.code = code
        self.salary = salary

    def __str__(self):
            return f'{self.name}, {self.address}, {self.code}, {self.salary}'
    
    
Aman = Employee('Aman', 'f 1054 barra 8', '202802', '300000')
print(Aman)