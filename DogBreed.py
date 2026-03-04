class Dog:

    species = "Canine"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def display_details(self):
        print("Name: {self.name}")
        print("Breed: {self.breed}")
        print("Species: {Dog.species}")

dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Max")

print("--- Dog Details --- ")
dog1.display_details()
dog2.display_details()