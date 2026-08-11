class pet:
    print('hi i am a pet profiler')
pet_object = pet()
class petprofile:
    category = 'pet'
    def __init__(self,name,animal_type,age,favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food
pet1 = petprofile('Jonny', 'Dog', 3, 'chicken')
pet2 = petprofile('Bob', 'Cat', 5, 'Salmon')
print('Jonny is a {}'.format(pet1.category))
print('Bob is a {}'.format(pet2.category))
print('{} is a {} and is {} years old'.format(pet1.name, pet1.animal_type, pet1.age))
print('{} likes to eat {}'.format(pet1.name, pet1.favourite_food))
print('{} is a {} and is {} years old'.format(pet2.name, pet2.animal_type, pet2.age))
print('{} likes to eat {}'.format(pet2.name, pet2.favourite_food))

