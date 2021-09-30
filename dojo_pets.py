class Pet:

    def __init__(self, name, type, tricks, health=0, energy=0):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print(f"{self.name} is sleeping.")
        self.energy += 25
        return self
    
    def eat(self):
        print(f"{self.name} is eating.")
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        print(f"{self.name} is eating.")
        self.health += 5
        return self

    def noise(self):
        if self.type == "cat":
            print("miau")
        elif self.type == "horse":
            print("ihaaa")
        elif self.type == "doggo":
            print("roof roof")
        else:
            print("What does a fox say?")
        return self

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"Walking my {self.pet.type}.")
        self.pet.play()
        return self

    def feed(self):
        print(f"Feeding my {self.pet.type}.")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"Bathing my {self.pet.type}.")
        self.pet.noise()
        return self

fluffy = Pet("Fluffy", "doggo", ["sit", "roll", "give paw"], 30, 100)
anna = Ninja('Anna', 'Mlo', 'sausage', 'meat', fluffy)

anna.feed().bathe().walk()
print("Anna's pets health: ", anna.pet.health, "Anna's pet's energy: ", anna.pet.energy)