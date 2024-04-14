
class Animal:
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age
    def details(self):
          print(f"the name of the Animal is {self.name},it's belongs to {self.species} and it's age is {self.age}")
              
class Lion(Animal):
        def lion(self,):
            print(f"The {self.name} is very dangerous")

class Elephant(Animal):
        def elephant(self):
            print(f"The {self.name} is very big in his family")

class Monkey(Animal):
        def monkey(self):
            print(f"The {self.name} is very clever")
        
#main code

Animal1 =Lion('Simba','Cat',20)
Animal2 =Elephant('Appu','Indian',30)
Animal3 =Monkey('Hira','macaques',15)



Animal1.details()
Animal2.details()
Animal3.details()
Animal1.lion()
Animal2.elephant()
Animal3.monkey()
