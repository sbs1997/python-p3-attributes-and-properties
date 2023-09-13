#!/usr/bin/env python3

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

class Dog:
    def __init__(self, name="Fido", breed = "Mastiff"):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        return self._name

    def set_name(self, input):
        if type(input) == str and 1<=len(input)<=25:
            self._name = input
        else:
            print("Name must be string between 1 and 25 characters.")    

    def get_breed (self):
        return self._breed
    
    def set_breed (self, input):
        if input in APPROVED_BREEDS:
            self._breed = input
        else:
            print("Breed must be in list of approved breeds.")
    
    name = property( get_name, set_name)
    breed = property (get_breed, set_breed)

# shosti = Dog("Burke")
# shosti.name = "Shosti"

# nameless = Dog("")