# simple list
motorcycles = ['honda', 'yamaha', 'suzuki']
empty_list = []
# access list elements
motorcycles[0]
motorcycles[-1]
# add element to the end of a list
motorcycles.append('ducati')
# modify existing element of a list
motorcycles[0] = 'mitsubishi'
# insert new element to a list
motorcycles.insert(1, 'kawasaki') # (index, value)
# remove element from a list (by index)
del motorcycles[0]
# removal using 'pop()' method (allows working with the removed item)
motorcycles.pop()  # removes the last item in a alist
motorcycles.pop(2)  # removes an item by index
# remove an item by value from a list (allows working with the removed item)
motorcycles.remove('kawasaki')
# sort alphabetically (permanent)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
# sort reverse alphabetically (permanent)
cars.sort(reverse=True)
# sort alphabetically (temporary)
sorted(cars)
# sort reverse alphabetically (temporary)
sorted(cars, reverse=True)
# reverse list chronologically (permanent)
cars.reverse()
# display length of a list
len(cars)
# looping thru a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone.  That was a great magic show!")
# 'range()' function (off-by-one behavior)
for value in range(6):  # counts from 0 to 5
    print(value)
for value in range(1, 6):  # counts from 1 to 5
    print(value)
# skipping numbers within a range (add 3rd argument)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)
# squares
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
# squares (list comprehension style)
squares = [value**2 for value in range(1, 11)]
print(squares)
# statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)  # returns the lowest value element
max(digits)  # returns the highest value element
sum(digits)  # returns the sum of the list
# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
players[0:3]
players[:4]  # ommiting 1st index starts slice at first element
players[2:]  # ommiting 2nd index ends slice at last element
players[-3:]
# looping through a slice
for player in players[:3]:
    print(player.title())
# copying a list
copy_players = players[:]
# a simple tuple
dimensions = (200, 50)
my_t = (3,)  # tuple with 1 element
# reassign variable to a tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
