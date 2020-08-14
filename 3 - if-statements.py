# simple if statement (1 conditional test, 1 action)
age = 19
if age >= 18:
    print("You are old enough to vote!")

# if-elif-else statements
active = True
while active:
    age = input("Welcome to Disney Land.  Please enter your age: ")
    if age == 'quit':
        active = False
    else:
        if int(age) < 4:
            price = 0
        elif int(age) < 18:
            price = 25
        elif int(age) < 65:
            price = 40
        else:
            price = 20
        print(f"Your Disney Land admission cost is ${price}.")

list_toppings = []
active = True
while active:
    requested_topping = "Add the desired toppings unto your pizza.\n"
    requested_topping += "(Enter 'done' when you are finished or 'cancel' if you want to cancel your order): "
    request = input(requested_topping)
    if request == 'cancel':
        active = False
    list_toppings.append(request)
    if request == 'done':
        list_toppings.remove('done')
        print(
            "\nFinished making your pizza!\nThe following toppings were added unto your pizza:")
        for topping in list_toppings:
            print(f"\t- {topping.title()}")
        active = False
    else:
        print(f"...Adding '{list_toppings[-1].title()}'")
        if request == 'done':
            list_toppings.remove('done')
            print("Your favorite fruits are:")
            for fruit in list_toppings:
                print(f"- {topping.title()} ")
            active = False
