# simple input function (style1)
print(input("Tell me something, and I will repeat it back to you: "))
# alternatively
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# multi-line string
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
# numerical input using 'int()'
age = int(input("How old are you? "))
print(type(age))
# modulo operator
number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
# while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# quit value in while loop
prompt = "\nTell me something, and I will repeat in back to you:"
prompt += "\nEnter 'quit' to tend the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# using a flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
# using 'break' in a loop
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
# using 'continue' in a loop
current_number = 0
   while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue
    print(current_number)
