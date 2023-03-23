# cat.py
# external imports
from random import choice

class ScratchPost:
    ''' ScratchPost is something a Cat object will interact with if they want to scratch

    Attributes
        hp: A scratch post has a total health point of 10
    '''
    def __init__(self):
        ''' initialization method to set hp attribute to 10 '''
        self.hp = 10

    def use(self):
        ''' the use method allows external objects to use the Scratch Post 
        
        returns True if the post was successfully used.
        '''
        if self.hp > 0:
            self.hp -= 1
            return True
        else:
            return False

    def __str__(self):
        ''' this is an __str__() override to allow str casting for ScratchPost '''
        return f'A scratch post. Scratches left: {self.hp}.'

    def __repr__(self):
        ''' __repr__() override to allow scratchpost to be represented in other objects '''
        return self.__str__()

class Cat:
    ''' Cat class representing cats

    Attributes
        name: cat's name
        breed: cat's breed
        colour: cat's colour
        is_hungry: is the cat hungry?
        wants_to_scratch: does the cat want to scratch?

    Methods
        eat(): allows the cat to eat when hungry
        scratch(): allows the cat to scratch a scratch post
    '''
    def __init__(self, name, breed, colour):
        ''' initialization of cats
        
        Arg:
            name: string value for the name attribute
            breed: string value for the breed attribute
            colour: string value for the colour attribute
        '''
        self.name = name
        self.breed = breed
        self.colour = colour
        self.is_hungry = choice([True, False])
        self.wants_to_scratch = choice([True, False])

    def eat(self, food):
        ''' eat() allows cat to eat food and satisfy its hunger condition
        
        Arg:
            food: string value for the food it is eating
        '''
        if self.is_hungry:
            print(f'{self.name} is eating {food}.')
            self.is_hungry = False
        else:
            print(f'{self.name} is not hungry.')

    def scratch(self, post):
        ''' scratch() allows cat to scratch a scratch post

        Arg:
            post: A ScratchPost object  
        '''
        if not self.wants_to_scratch:
            print(f'{self.name} does not need to scratch.')
        else:
            if post.use():
                self.wants_to_scratch = False
                print(f'{self.name} scratched the post.')
            else:
                print('This post cannot be scratched anymore.')