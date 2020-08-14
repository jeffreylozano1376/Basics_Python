# Person
person_info = {"first_name": "Jeffrey", "last_name": "Lozano",
               "age": 29, "city": "Mandaluyong City"}
print(person_info)

# Favorite Numbers
friends = {
    'jastin': '6',
    'gabriel': '1',
    'julius': '5',
    'shem': '9'
}
for name, number in friends.items():
    print(f"{name.title()}'s favorite number is {number}.")

# Glossary
programming_words = {
    'list': 'a data structure in Python that is a mutable, or changeable, ordered sequence of elements',
    'tuple': 'like a list, it is sequence of Python objects, however it is immutable',
    'set': 'an unordered collection data type that is iterable, mutable and has no duplicate elements',
    'dictionary': 'maps a set of objects (keys) to another set of objects (values)',
}
for word, definition in programming_words.items():
    print(f"\n{word.upper()}:", end="")
    print(f"\t{definition}")

# Rivers
rivers = {
    'nile river': [
        'egypt', 'sudan', 'south sudan', 'eritrea', 'ethiopia', 'kenya', 'congo', 'burundi', 'rwanda', 'uganda', 'tanzania'],
    'amazon river': [
        'peru', 'bolivia', 'venezuela', 'colombia', 'ecuador', 'brazil'],
    'yangtze river': ['china']
}
for river, countries in rivers.items():
    print(f"The {river.title()} runs through the following countries:")
    for country in countries:
        print(f"- {country.title()}")

# Polling
join_poll = ['jeffrey', 'ken', 'sevan', 'joan']
respondent = ['jeffrey', 'ken']
for joinee in join_poll:
    if joinee in respondent:
        print(f"Thank you {joinee.title()} for responding.")
    else:
        print(f"{joinee.title()} please take the poll!")

# People (complex)
person_info = {
    'person_1': {
        "first_name": "Jeffrey",
        "last_name": "Lozano",
        "age": "29",
        "city": "San Mateo, Rizal"
    },
    'person_2': {
        "first_name": "Ken",
        "last_name": "Hufancia",
        "age": "26",
        "city": "Naga City"
    },
    'person_3': {
        "first_name": "Gabriel",
        "last_name": "Tiongson",
        "age": "28",
        "city": "Marikina City"
    }
}
for person_info, info in person_info.items():
    print(f"{person_info}:")
    print(f"\t-{info['first_name']}")
    print(f"\t-{info['last_name']}")
    print(f"\t-{info['age']}")
    print(f"\t-{info['city']}")
