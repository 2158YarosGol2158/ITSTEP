# # class Animal:
# #     def sound(self):
# #         pass #пусто
# #
# # class Dog(Animal):
# #     def sound(self):
# #         return "Гав"
# #
# # class Cat(Animal):
# #     def sound(self):
# #         return "Мяу"
# #
# #
# # class Cow(Animal):
# #     def sound(self):
# #         return "Му"
# #
# # def speak(an):
# #     print(an.sound())
# #
# # a1=Dog()
# # a2=Cat()
# # a3=Cow()
# # speak(a1)
# # speak(a2)
# # speak(a3)
#
# # class Pay:
# #     def process(self,money):
# #         pass
# #
# # class Credit(Pay):
# #     def process(self,money):
# #         return "Оплата "+str(money)+" грн здійснена через кредитну картку"
# #
# # class Cash(Pay):
# #     def process(self,money):
# #         return "Оплата "+str(money)+" грн здійснена через готівку"
# #
# # class System(Pay):
# #     def process(self,money):
# #         return "Оплата "+str(money)+" грн здійснена через онлайн систему"
# #
# # buy=[Credit(),Cash(),System()]
# # num=int(input("Введіть суму покупки: "))
# # for k in buy:
# #     print(k.process(num))
# # class Dog:
# #     def __init__(self,name):
# #         self.name=name
# #
# # #public
#
#
# # dog1=Dog("Бані")
# # print(dog1.name)
# #
# # #private
# #
# # class Dog:
# #     def __init__(self,name):
# #         self.name=name
# #         self.__age=2
# #     def info(self):
# #         return self.__age
# #
# # dog1=Dog("Бані")
# # print(dog1.info())
# #
# # #protected
#
# # class Dog:
# #     def __init__(self,name):
# #         self.name=name
# #         self.__age=2
# #         self._breed="бульдог"
# #
# # class D(Dog):
# #     def info(self):
# #         return  "Це щеня породи "+self._breed
# #
# # dog1=D("Бані")
# # print(dog1.info())
#
# class Person:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self._age=age
#         self.__salary=salary
#
#     def info(self):
#         print("Мене звати",self.name)
#         self._infoAge()
#         self.__infoSalary()
#
#     def _infoAge(self):
#         print("Мій вік", self._age)
#     def __infoSalary(self):
#         print("Моя зп", self.__salary)
#
# class Employee(Person):
#     def __init__(self,name,age,salary,pos):
#         super().__init__(name,age,salary)
#         self.pos=pos
#     def printInfo(self):
#         print("Моя посада",self.pos)
#         print("Мій вік",self._age)
#         # print("Моя ЗП", self.__salary) помилка
#
# human=Person("Олеся",20,2000)
# worker=Employee("Петро",25,45000,"Інженер")
# print(human.name)
# human.info()
# print(worker.name)
# worker.printInfo()
# print(worker._age)
# print(worker._Person__salary)

import random as r
class Character:
    def __init__(self,name):
        self.__name = name
        self.__health = r.randint(1,101)
    def infoName(self):
        return self.__name
    def infoHP(self):
        return self.__health
    def attack(self,num):
        pass
    def take_degame(self):
        self.__health-=r.randint(1,11)
    def is_alive(self):
        return self.__health>0
    def __str__(self):
        return self.__name+" має здоров'я "+str(self.__health)

class Warrior(Character):
    def __init__(self,name,health=100):
        super().__init__(name,health)


    def attack(self,num):
        print(self.__name+" атакує мечем")
        num.take_degame(r.randint(10,21))

class Mage(Character):
    def __init__(self,name,health):
        super().__init__(name,health)
        self.__health=r.randint(20,80)

    def attack(self,num):
        print(self.__name+" атакує магією")
        num.take_degame(r.randint(20,26))

# Завдання 2

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.__title = title
        self.__author = author
        self.__item_id = item_id
        self.__is_taken = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_item_id(self):
        return self.__item_id

    def is_same_item(self, other_item):
        return self.__item_id == other_item.get_item_id()

    def display_info(self):
        pass

    def take_item(self):
        if self.__is_taken:
            print(f"Матеріал '{self.__title}' вже взятий.")
        else:
            self.__is_taken = True
            print(f"Ви взяли '{self.__title}'.")

    def return_item(self):
        if self.__is_taken:
            self.__is_taken = False
            print(f"Ви повернули '{self.__title}'.")
        else:
            print(f"Матеріал '{self.__title}' вже знаходиться в бібліотеці.")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.__pages = pages

    def display_info(self):
        print(f"Книга: {self.get_title()}, Автор: {self.get_author()}, Сторінки: {self.__pages}")

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.__issue_number = issue_number

    def display_info(self):
        print(f"Журнал: {self.get_title()}, Автор: {self.get_author()}, Номер випуску: {self.__issue_number}")

class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.__duration = duration

    def display_info(self):
        print(f"Аудіокнига: {self.get_title()}, Автор: {self.get_author()}, Тривалість: {self.__duration} хвилин")

library = [
    Book("Майстер і Маргарита", "Булгаков", 1, 320),
    Magazine("Наука і життя", "Редакція", 2, 202),
    Audiobook("1984", "Джордж Орвелл", 3, 670)
]

for item in library:
    item.display_info()
    item.take_item()
    item.return_item()
    print("---")

b1 = Book("Майстер і Маргарита", "Булгаков", 1, 320)
b2 = Book("Щось інше", "Інший автор", 1, 150)
print("Це той самий об’єкт за ID?", b1.is_same_item(b2))