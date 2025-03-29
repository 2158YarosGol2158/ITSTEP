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
