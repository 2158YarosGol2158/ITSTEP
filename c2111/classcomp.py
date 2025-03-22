# class People:
#     count=0
#     def __init__(self,name="Vasya"):
#         self.name=name
#         People.count+=1
# class Bus:
#     def __init__(self,brend):
#         self.brend=brend
#         self.passenger=[]
#     def add(self,*args):
#         for n in args:
#             self.passenger.append(n)
#     def info(self):
#         if self.passenger==[]:
#             print("Пасажири відсутні у ",self.brend)
#         else:
#             print("Пасажири присутні у ",self.brend,": ")
#             for n in self.passenger:
#                 print(n.name)
#
# pass1=People()
# pass2=People("Лена")
# pass3=People("Саня")
# bus1=Bus("Богдан")
# bus1.add(pass1,pass2,pass3)
# # bus1.add(pass2)
# bus1.info()
# print(People.count)

# class Human:
#     def __init__(self,name,age,height,city,animal):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.city=city
#         self.animal=animal
#     def __str__(self):
#         return "Вітаю! Я "+self.name+", мені "+str(self.age)+" років, маю зріст "+str(self.height)+". Я з міста "+self.city+". Маю тварин: "+self.animal
#
# class People(Human):
#     def __init__(self,name,age,height,city,animal,school,clas):
#         super().__init__(name,age,height,city,animal)
#         self.school=school
#         self.clas=clas
#     def __str__(self):
#         return super().__str__()+". Навчаюсь у школі "+str(self.school)+" у "+str(self.clas)+" класі"
# class Worker(Human):
#     def __init__(self, name, age, height, city, animal, job, salary):  # new *
#         super().__init__(name, age, height, city, animal)
#         self.job = job
#         self.salary = salary
#
#     def __str__(self):  # new *
#         return super().__str__() + ". Працюю на посаді " + self.job + ", маю зп " + str(self.salary) + "$"
#
#
# h=Human("Маша",16,156,"Київ","Кіт")
# p=People("Олег",14,154,"Львів","Папуга",111,5)
# W = Worker("Яна", 35, 168, "Харків", "немає", "дизайнер", 3500)
#
#
# print(str(h.__str__()))
# print(str(p))
# print(str(W))


class PC:
    def __init__(self, model="HP"):
        super().__init__()
        self.model = model
        self.memory = 256

class Display:
    def __init__(self):
        super().__init__()
        self.res = '4K'

class Smart(PC, Display):
    def info(self):
        print('Смартфон моделі', self.model, "має об'єм пам'яті", self.memory, 'Гб та розширення екрана', self.res)

tel = Smart('Samsung')
tel.info()
