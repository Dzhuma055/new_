# class 
#     money = 100
# user = Person()
# print(user.money)

# user1 = Person()
# print(user1.money)
# user.money = 200
# print(user.money)




# class Person:
#     name = ''
#     money = 0

# person1 = Person()
# person2 = Person()


# person1.name = 'Erkin'
# person2.name = 'Alibek'


# person1.money = 100
# person2.money = 0

# print(person1.name, person1.money)
# print(person2.name, person2.money)



# class Critter:
#     total = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Critter.total += 1
#         print(f'Появилось новое животное {name}')

#     def talk(self):
#         print(f"hello, my name is {self.name}")


#     @staticmethod
#     def status():
#         print(f"Сейчас всего {Critter.total} животных ")


# pet = Critter('Barboss', 4)
# pet = Critter('Murzik', 2)
# pet.talk()
# Critter.status()

# class Mylist(list):
    
#     def my_method(self):
#         print('My cystom list')
        
# list1 = Mylist()

# list1.append(44)
# list1.insert(0, 1)
# list1.insert(1, 2)
# list1.insert(2, 3)

# print(list1)
# print(type(list1))



# class Dog:
#     total = 0
#     def __init__(self, name, age, hunger=0):
#         self.name = name
#         self.age = age
#         self.hunger = hunger
#         Dog.total += 1
#         print(f"created new object of class Dog")
#         print(f"total objects of class {Dog.total}")

#     def _pass_time(self):
#         self.hunger += 1

#     def talk(self):
#         print(f"My name is {self.name}")
#         self._pass_time()
    
#     def eat(self):
#         print("Thanks")
#         self.hunger -= 2
#         self._pass_time()
    
#     def walk(self):
#         print(f"i like to walk")
#         self._pass_time()

#     def status(self):
#         print(f"hunger: {self.hunger}")

# dog = Dog("Gray", 2, 3)


# class Dachshund(Dog):
#     # def _pass_time(self):
#     #     self.hunger += 1

#     def talk(self, text):
#         print(text)
#         self._pass_time()
    
#     def sleep(self):
#         print("Zzzzz")
#         self._pass_time()

# mini_dog = Dachshund('Dog', 3)
# mini_dog.sleep()
# mini_dog.eat()
# mini_dog.talk('gav gav')
# dog.talk()
# dog.eat()
# dog.status()
# mini_dog.status()
            
# class Avto:
#     def ride(self):
#         print("Riding on a ground")
#
# class Boat:
#     def swim(self):
#         print("Sailing in the ocean")
#
# class Amphibian(Avto, Boat):
# a = Amphibian()
#
# a.swim()
# a.ride()

#
# class MusikPlayerMixin:
#     def play_musik(selfself, song):
#         print(f"Now playong: {song}")
#
# class Smartphone(MusikPlayerMixin):
#     pass
#
# class Radio(MusikPlayerMixin):
#     pass
#
# class Avto(MusikPlayerMixin):
#     pass
# a = Smartphone()
# a.play_musik("lalala")
# b = Avto()
# b.play_musik("lalala")
#
# Now playong: lalala
# Now playong: lalala