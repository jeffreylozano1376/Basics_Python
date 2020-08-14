# Rental Car
car_prompt = input("What kind of rental car do you like? ")
print(f"Let me see if I can find you a {car_prompt.title()}")

# Restaurant Seating
seating_prompt = int(input("How many people are there in your dinner group? "))
if seating_prompt > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# Multiples of Ten
number_prompt = int(input(
    "Tell me a number and I will tell you if the number is a multiple of 10 or not. "))
given_number = number_prompt % 10
if given_number == 0:
    print("It is a multiple of 10")
else:
    print("It is NOT a multiple of 10")

# Pizza Toppings
prompt = "Please enter the toppings you want to add unto your pizza."
prompt += "(Enter 'quit' when you are done): "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Movie Tickets
prompt = "Ticket price varies according to age."
prompt += "\nPlease enter your age: "
person_age = int(input(prompt))
ticket = ""
active = True
while active:
    message = input(prompt)
    if person_age < 3:
        ticket = "$ 0"
        print(ticket)
    elif person_age == 3 <= 12:
        ticket = "$ 10"
        print(ticket)
    else:
        ticket = "$ 15"
        print(ticket)
