class Human():
    def __init__(self,name,birthday,gender,weight,height):
        self.name = name 
        self.birthday = birthday
        self.gender = gender  
        self.weight = weight
        self.height = height
    def bmi(self):
        b = self.weight / self.height / self.height
        return b 
person_1 = Human("Jobs","February 24,1955","male",75,1.78)

print(person_1.name)
print(person_1.birthday)
print(person_1.gender)

print(person_1.bmi())

