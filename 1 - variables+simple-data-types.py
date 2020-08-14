# Variable + Print + 'End' parameter
message_0 = "Hello World! "
message_1 = "Hello Python World"
print(message_0, end="")
print(message_1)
# Strings (single / double quoting)
message_2 = 'I told my friend, "Python is my favorite language"'
message_3 = "The language 'Python' is named after Monty Python, not the snake."
# 'Escape' character
message_4 = 'One of Python\'s greatest strengths is its diverse and supportive community.'
# Casing
name = "jeffrey lozano"
print(name.title())  # title casing
gender = "MALE"
print(gender.lower())  # lower casing
location = "manila"
print(location.upper())  # upper casing
# f-strings
first_name = "jeffrey"
last_name = "lozano"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
# whitespace
print("Languages:\n\tPython\n\tJavaScript\n\tC")
# stripping whitespace
programming_language = ' python '
print(programming_language.rstrip())
print(programming_language.lstrip())
print(programming_language.strip())
# integers & flaots
print(4/2)  # integer / integer = float
print(4//2)  # integer // integer = integer
print(10/2.5)  # integer / float = float
print(10//2.5)  # integer // float = float
print(3.0 ** 2)  # integer +-*/ float = float
# underscores
universe_age = 14_000_000_000
my_age = 2_9
print(universe_age, my_age)
# multiple assignment
x, y, z = 0, 1, 2
print(x, y, z)
# constants
MAX_CONNECTIONS = 5000  # python convention on constants
print(MAX_CONNECTIONS)
