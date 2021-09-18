class Animal:
    def __init__(self,name):
        self.name = name


class Zoo:
    def __init__(self,name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self,species,name):
        if species == 'mammal':
            self.mammals.append(name)
        if species == 'fish':
            self.fishes.append(name)
        if species == 'bird':
            self.birds.append(name)

    def get_info(self,species):
        if species == 'mammal':
            animals = self.mammals
            species_name_plural = 'Mammals'
        elif species == 'fish':
            animals = self.fishes
            species_name_plural = 'Mammals'
        elif species == 'bird':
            animals = self.birds
            species_name_plural = 'Mammals'
        return(
            f'{species_name_plural} in {self.name}: {", ".join([animal.name for animal in animals])}\nTotal animals: {animal_count}'
        )


zoo_name = input()
animal_count = int(input())
zoo=Zoo(zoo_name)
for i in range(animal_count):
    species,animal_name = input().split(" ",maxsplit=1)
    animal = Animal(animal_name)
    zoo.add_animal(species,animal)


print(zoo.get_info(input()))

