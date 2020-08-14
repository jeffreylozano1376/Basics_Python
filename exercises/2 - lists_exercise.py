# Guest List
dinner_invites = ['jeffrey', 'ken', 'hany']
print(f"Hi {dinner_invites[0].title()}, you are invited to dinner.")
print(f"Hi {dinner_invites[1].title()}, you are invited to dinner.")
print(f"Hi {dinner_invites[2].title()}, you are invited to dinner.")
# Changing Guest List
print(
    f"{dinner_invites[-1].title()} just called.  She won't be attending dinner. ")
dinner_invites[2] = "nikki"
print(f"Rather, she would be replaced by {dinner_invites[2].title()}.")
print("Hence, here are the final attendees:")
print(f"\t- {dinner_invites[-3].title()}")
print(f"\t- {dinner_invites[-2].title()}")
print(f"\t- {dinner_invites[-1].title()}")
# Shrinking Guest List
print("Unfortunately, the dinner table is only good for one person.")
popped_1 = dinner_invites.pop(1)
print(f"I'm sorry {popped_1.title()}, your invitation has been cancelled.")
popped_2 = dinner_invites.pop(1)
print(f"I'm sorry {popped_2.title()}, your invitation has been cancelled.")
print(f"{dinner_invites[0].title()}, you are still invited.")
del dinner_invites[0]
print(dinner_invites)
# Seeing the World
places_to_visit = ['pyramids_of_giza', 'stone_henge',
                   'machu_picchu', 'easter_island', 'pyramid_of_the_sun']
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)
print(f"There are {len(places_to_visit)} places I want to visit.")
# Pizzas
pizzas = ['cheese pizza', 'pepperoni pizza', 'hawaiian pizza']
for pizza in pizzas:
    print(f"I like {pizza.title()}")
print("I really love pizza")
# Animals
animals = ['lion', 'tiger', 'jaguar']
for animal in animals:
    print(f"A {animal.title()} would make a great pet")
print("Any of these animals would make a great pet!")
# Counting to Twenty
for value in range(1, 21):
    print(value)
# One Thousand
thousands = []
for value in range(1, 1_001):
    thousands.append(value)
print(thousands)
# Summing a Million
millions = []
for value in range(1, 1_000_001):
    millions.append(value)
print(min(millions))
print(max(millions))
print(sum(millions))
# Odd Numbers (using 'for' loop)
odd_numbers = []
for value in range(1, 20, 2):
    odd_numbers.append(value)
print(odd_numbers)
# Odd Numbers (using class 'list')
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)
# Threes (using 'for' loop)
multiples_3 = []
for value in range(3, 31, 3):
    multiples_3.append(value)
print(multiples_3)
# Threes (using class 'list')
multiples_3 = list(range(3, 31, 3))
print(multiples_3)
# Cubes (using 'for' loop)
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)
# Cubes (using class 'list comprehension')
cubes = list(cube**3 for cube in range(1, 11))
print(cubes)
# Slices
print(animals)
print(f"The first 2 items of the the list are {animals[:2]}.")
print(f"The last 2 items of the the list are {animals[-2:]}.")
print(places_to_visit)
print(
    f"The three items from the middle of the list are {places_to_visit[1:4]}.")
print(pizzas)
print(f"The last 2 items of the list are {pizzas[-2:]}.")
# My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
print(pizzas)
pizzas.append('meat lovers')
print(pizzas)
friend_pizzas.append('veggie loves')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"\t- {pizza.title()}")
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t- {pizza.title()}")
