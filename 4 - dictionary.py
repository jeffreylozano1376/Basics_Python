# simple dictionary
dictionary = {'key1': 'value1', 'key2': 'value2'}
empty_dictionary = {}
# access dictionary values
dictionary['key1']
dictionary['key2']
# add key-value pair to a dictionary
dictionary['key3'] = 'value3'
# modify dictionary value
dictionary['key3'] = 'value4'
# remove key-value pairs
del dictionary['key3']
# clean & pythonic dictionary
fave_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# access dictionary value using 'get()'
get_info1 = fave_language.get('jen', 'info does not exist')  # returns 1st arg
get_info2 = fave_language.get('jeffrey', 'info does not exist')  # returns 2nd
get_info3 = fave_language.get('ken')  # returns 'None'
# loop through all 'key-value pairs' of a dictionary
for name, language in fave_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# loop through all 'keys' of a dictionary
for name in fave_language.keys():
    print(name.title())
for name in fave_language:  # 'for loop' default return
    print(name.title())
# loop through all 'values' of a dictionary
for language in fave_language.values():
    print(language.title())
for language in set(fave_language.values()):  # unique values
    print(language.title())
# dictionaries in list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# auto-populating dictionaries in lists
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")
# lists in dictionary (example 1)
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(
    f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
# lists in  dictionary (example 2)
fave_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
for name, languages in fave_language.items():
    print(f"\n{name.title()}'s' favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
# dictionary in dictionary
users = {
    'aeinsten': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    print(
        f"\tFullname: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"\tLocation: {user_info['location']}")
