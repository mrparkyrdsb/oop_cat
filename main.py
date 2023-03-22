# Main.py
from cat import Cat
from cat import ScratchPost

post = ScratchPost()
cat1 = Cat('Cheetos', 'Tabby', 'Orange')

# cat data
print(cat1)

# post data
print(post)

# is cat1 hungry?
print(cat1.is_hungry)
cat1.eat('tuna')

# does cat1 need to scratch?
print(cat1.wants_to_scratch)
cat1.scratch(post)

print(post)
