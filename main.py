# Main.py
# from FILENAME_WITHOUT_EXTENSION import CLASSNAME
from cat import Cat # Cat class from cat.py
from cat import ScratchPost # ScratchPost class from cat.py

post = ScratchPost() # a scratchpost object (class instance)
cat1 = Cat('Cheetos', 'Tabby', 'Orange') # a cat object

# cat data
print(cat1)

# post data
print(post)

# is cat1 hungry?
print(cat1.is_hungry) # accessing an attribute: .is_hungry
cat1.eat('tuna')

# does cat1 need to scratch?
print(cat1.wants_to_scratch) # accessing an attribute ._wants_to_scratch
cat1.scratch(post) # cat object interacting with a post object

# rechecking post data
print(post)
