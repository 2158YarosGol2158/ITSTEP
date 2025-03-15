# class Car:
#     # speed=110
#     def __init__(self,speed):
#         self.speed=speed
#     def info(self):
#         print("Швидкість авто: ",self.speed)
# sp=int(input("Максимальна швидкість авто: "))
# auto = Car(sp)
# # print("Швидкість авто:",auto.speed)
# auto.info()
# auto2=Car(180)

class Pupils:
    count=0
    def __init__(self,name,height):
        self.name=name
        self.height=height
        Pupils.count+=1
    def __str__(self):
        print("Ім'я учасника: ",self.name, " Зріст: ", self.height)

pl1=Pupils("Ігор",155)
pl1.__str__()
pl2=Pupils("Оля",134)
pl2.__str__()
pl3=Pupils("Кіра",163)
pl3.__str__()
print(pl1.count, " учасника змагань")