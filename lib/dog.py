#!/usr/bin/env python3


class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="Fido", breed="Pug"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in Dog.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")






# # Practice work
# class Human:
#     species = "Homo Sapiens"
#     def __init__(self, name):
#         self.name = name


# # print(Human.species)

# class Best:
#     food = "yummy"
#     fave = "sushi"
#     def __init__(self, name="sushi"):
#         self.name = name

# # print(Best.food)

# fave_food = Best("sushi")
# # print(fave_food.name)
# # print(Best.fave)

# Best2=Best("ramen")
# # print(Best2.name)
# # print(f"I love {Best2.name}")


# class Human:
#     species = "Homo sapiens"

#     def __init__(self, age):
#         self.age = age  # Calls the setter below

#     @property
#     def age(self):
#         print("Retrieving age.")
#         return self._age

#     @age.setter
#     def age(self, value):
#         print(f"Setting age to {value}")
#         self._age = value

    


# # her_age = property(set_age("27"))
# # her = Human(25)
# # print(her.age)

# her = Human(30)  #prints set_age = Setting age to 30
# # her.age = 30
# print(her.age)   #prints Setting age to 30 and Retrieving age and 30



