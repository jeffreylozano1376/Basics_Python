# Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
# Alien Colors # 1
run_program = True
while run_program:
    alien_color = input("Alien Color: ")
    if alien_color == 'quit game':
        run_program = False
    else:
        if alien_color == 'green':
            points = 5
        elif alien_color == 'yellow':
            points = 10
        elif alien_color == 'red':
            points = 15
        print(f"You just earned {points} points.")
# Stages of Life
run_program = True
while run_program:
    person_age = input(
        "To determine the current life stage, please input age: ")
    if person_age == 'exit program':
        run_program = False
    else:
        if int(person_age) < 2:
            life_stage = 'baby'
        elif int(person_age) < 4:
            life_stage = 'toddler'
        elif int(person_age) < 13:
            life_stage = 'kid'
        elif int(person_age) < 20:
            life_stage = 'teenager'
        elif int(person_age) < 65:
            life_stage = 'adult'
        elif int(person_age) > 64:
            life_stage = 'elder'
        print(f"The person is a '{life_stage.lower()}'.")
# Favorite Fruit
list_fruits = []
active = True
while active:
    fruit_prompt = "What are your favorite fruits?\n"
    fruit_prompt += "(type 'done' when you are done): "
    response = input(fruit_prompt)
    if response == 'cancel':
        active = False
    list_fruits.append(response)
    if response == 'done':
        list_fruits.remove('done')
        print("Your favorite fruits are:")
        for fruit in list_fruits:
            print(f"- {fruit.title()} ")
        active = False
    else:
        print(f"...Adding '{list_fruits[-1].title()}'")
        if response == 'done':
            list_fruits.remove('done')
            print("Your favorite fruits are:")
            for fruit in list_fruits:
                print(f"- {fruit.title()} ")
            active = False
# Hello Admin
usernames = ['admin', 'jlo1376', 'jeffreylozano1376',
             '50shapesofgrape', '50snakesaregreat']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging again.")
# No Users
users = []
if users:
    for user in users:
        print(f"Hello {user}.")
else:
    print("We need to find some users!")
# Checking usernames
current_users = ['admin', 'jlo1376', 'jeffreylozano1376',
                 '50shapesofgrape', '50snakesaregreat']
new_users = ['Jlo1376', 'JEFFREYLOZANO1376',
             'cliffyshavesagreek', '50mouldsofclay', '50shadesofgrey']
lower = []
for current_user in current_users:
    lowered = current_user.lower()
    lower.append(lowered)
print(lower)
upper = []
for current_user in current_users:
    uppered = current_user.upper()
    upper.append(uppered)
print(upper)

for new_user in new_users:
    if new_user in current_users or lower or upper:
        print("The username already exists, please enter a new one.")
    else:
        print("The username is available.")

# Ordinal Numbers:
