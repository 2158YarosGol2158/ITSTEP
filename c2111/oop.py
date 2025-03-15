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

# class Pupils:
#     count=0
#     def __init__(self,name,height):
#         self.name=name
#         self.height=height
#         Pupils.count+=1
#     def __str__(self):
#         print("Ім'я учасника: ",self.name, " Зріст: ", self.height)
#     def __bool__(self):
#         return self.name != None
#     def __len__(self):
#         return self.height
#
# pl1=Pupils("Ігор",155)
# pl1.__str__()
# pl2=Pupils("Оля",134)
# pl2.__str__()
# pl3=Pupils("Кіра",163)
# pl3.__str__()
# print(pl1.count, " учасника змагань")
# print(pl1.__bool__())
# print(len(pl3))

import random as r

class Student:
    def __init__(self,name):
        self.name=name
        self.happy=r.randint(10,100)
        self.progres=r.randint(0,10)
        self.alive=True
    def study(self):
        print("Час для навчання")
        self.happy-=r.randint(1,5)
        self.progres+=r.randint(1,10)
    def sleep(self):
        print("Час для сну")
        self.happy+=r.randint(1, 5)
    def chill(self):
        print("Час для відпочинку")
        self.happy+=r.randint(50,100)
        self.progres-=r.randint(1, 10)
    def isAlive(self):
        if 1<self.progres<5:
            print("Ти на грані відрахувавння. Йди, навчайся")
            self.alive=False
        elif self.progres<=1:
            self.alive=False
            print("ВІДРАХОВАНИЙ!")
        elif self.progres>=5:
            print("Молодець")
            self.alive=True
    def everyday(self):
        print("Рівень щастя: ", self.happy)
        print("Прогрес навчання: ", self.progres)
    def studyLove(self,day):
        day="\nДень №"+str(day)
        print(day)
        res=r.randint(1,3)
        if res == 1:
            self.study()
        elif res == 2:
            self.sleep()
        elif res == 3:
            self.chill()
        self.everyday()
        self.isAlive()

st1=Student("Олег")
# print(st1.progres)
print("Життя студента",st1.name)
for c in range(1,8):
    if st1.alive==False:
        break
    st1.studyLove(c)
