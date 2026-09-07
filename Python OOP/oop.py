class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed 
        self.owner = owner
    def bark(self):
        print("whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name 
        self.address = address
        self.phone_number = contact_number
        
owner1= Owner("Danny", "122 Springfield Drive", "888-999")
dog1 = Dog("Bruce","German Shepherd", owner1)
print(dog1.owner.name)

owner2= Owner("Sally", "122 Springfield Drive", "888-999")
dog2 = Dog("Freya", "Greyhound", owner2)
print(dog2.owner.name)
