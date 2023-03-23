# p1
from random import choice # importing a choice method from the random module

class ScratchPost:
    def __init__(self):
        self.hp = 10

    def use(self):
        if self.hp <= 0:
            return False
        else:
            self.hp = self.hp - 1 # self.hp -= 1
            return True

    def __str__(self):
        return f'A Scratch Post. HP: {self.hp}.'

    def __repr__(self):
        return self.__str__()

class Cat:
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.is_hungry = choice([True, False])
        self.want_to_scratch = choice([True, False])

    def eat(self, food_name):
        if self.is_hungry:
            print(f'{self.name} ate {food_name}.')
            self.is_hungry = False
        else:
            print(f'{self.name} is not hungry.')

    def scratch(self, post):
        if self.want_to_scratch:
            if post.use():
                self.want_to_scratch = False
                print(f'{self.name} scratched {post}.')
            else:
                print(f'{post} is dead.')
        else:
            print(f'{self.name} does not need to scratch.')

    def __str__(self):
        return f'A {self.breed} cat named {self.name}.'

    def __repr__(self):
        return self.__str__()
        