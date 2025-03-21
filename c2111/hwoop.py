# Завдання 1
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def getinfo(self):
        print("Рік випуску:", self.year,"Марка:",self.make,"Модель:",self.model)

car1=Car("Рено", "Дастер", 2023)
car1.getinfo()

# Завдання 2
class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def get_salary_info(self):
        print(f"Заробітна плата {self.name}: {self.salary}")

employee1=Employee("Олег", "Директор", 100)
employee2=Employee("Лена", "Прибиральниця", 1000000000)
employee1.get_salary_info()
employee2.get_salary_info()
