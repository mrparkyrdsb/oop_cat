# cat.py
# external imports
from random import choice

class ScratchPost:
    def __init__(self):
        self.hp = 10

    def use(self):
        if self.hp > 0:
            self.hp -= 1
            return True
        else:
            return False

    def __str__(self):
        return f'A scratch post. Scratches left: {self.hp}.'

    def __repr__(self):
        return self.__str__()

class Cat:
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.is_hungry = choice([True, False])
        self.wants_to_scratch = choice([True, False])

    def eat(self, food):
        if self.is_hungry:
            print(f'{self.name} is eating {food}.')
            self.is_hungry = False
        else:
            print(f'{self.name} is not hungry.')

    def scratch(self, post):
        if not self.wants_to_scratch:
            print(f'{self.name} does not need to scratch.')
        else:
            if post.use():
                self.wants_to_scratch = False
                print(f'{self.name} scratched the post.')
            else:
                print(f'{self.name} destroyed this post and cannot scratch it anymore.')