class Person:
    def __init__(self, living, age, gender):
        self.living = living
        self.age = age
        self.gender = gender

    def getGender(self):
        result = self.gender
        return result

    def __str__(self):
        return str(self.living) + str(self.age) + str(self.gender)
        

a = Person(False, 29, 'female')
b = Person(True, 11, 'male')

print(a)
print(b)
