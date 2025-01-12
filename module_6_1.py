class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    pass

class Predator(Animal):
    def eat(self, food):
        super().eat(self, food)

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, edible=False)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)


wolf = Predator('Волк с Уолл-стрит')
hatiko = Mammal('Хатико')
flower = Flower('Цветик семицветик')
apple = Fruit('Заводной апельсин')

print(wolf.name)
print(hatiko.name)

print(wolf.alive)
print(hatiko.fed)

wolf.eat(flower)

hatiko.eat(apple)

print(wolf.alive)
print(hatiko.fed)