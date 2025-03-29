# class Animal:
#     def sound(self):
#         pass #пусто
#
# class Dog(Animal):
#     def sound(self):
#         return "Гав"
#
# class Cat(Animal):
#     def sound(self):
#         return "Мяу"
#
#
# class Cow(Animal):
#     def sound(self):
#         return "Му"
#
# def speak(an):
#     print(an.sound())
#
# a1=Dog()
# a2=Cat()
# a3=Cow()
# speak(a1)
# speak(a2)
# speak(a3)

# class Pay:
#     def process(self,money):
#         pass
#
# class Credit(Pay):
#     def process(self,money):
#         return "Оплата "+str(money)+" грн здійснена через кредитну картку"
#
# class Cash(Pay):
#     def process(self,money):
#         return "Оплата "+str(money)+" грн здійснена через готівку"
#
# class System(Pay):
#     def process(self,money):
#         return "Оплата "+str(money)+" грн здійснена через онлайн систему"
#
# buy=[Credit(),Cash(),System()]
# num=int(input("Введіть суму покупки: "))
# for k in buy:
#     print(k.process(num))