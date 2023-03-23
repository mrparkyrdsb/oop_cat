# p2
from random import choice

class ScratchPost:
    def __init__(self):
        self.hp = 10

    def use(self):
        if self.hp > 0:
            self.hp = self.hp - 1 # self.hp -= 1
            print('Scratch Post scratched successfully.')
            return True
        else:
            print('Scratch Post cannot be scratched.')
            return False

    def __str__(self):
        return f'A Scratch Post. HP: {self.hp}.'

    def __repr__(self):
        return self.__str__()

class Cat:
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.is_hungry = choice([True,False])
        self.want_to_scratch = choice([True,False])

    def eat(self, food_item):
        if self.is_hungry:
            print(f'{self.name} is eating {food_item}.')
            self.is_hungry = False
        else:
            print(f'{self.name} is not hungry.')

    def scratch(self, post):
        if self.want_to_scratch:
            if post.use():
                self.want_to_scratch = False
            else:
                print(f'{self.name} has nothing to scratch.')
        else:
            print(f'{self.name} does not need to scratch.')
    