# T-Shirt
def make_shirt(text='I love Python', size='large'):
    """Accepts a size and text of a message print for a shirt."""
    print(
        f"The size of the shirt is {size} and the message print is '{text}'.")


make_shirt('seek discomfort', 'small')
make_shirt()
# Cities


def describe_city(city, country="iceland"):
    """Accepts the name of a city and its country."""
    print(f"{city.title()} is in {country.title()}.")


describe_city('reykjavik')

# City Names


def city_country(city, country):
    """Accepts a name of a city and its country and returns a formatted string"""
    return print(f"{city.title()}, {country.title()}")


city_country("Manila", "Philippines")
city_country("Tokyo", "Japan")
city_country("Beijing", "China")

# Album


def make_album(artist_name, album_title, number_songs=None):
    """Builds a dictionary describing a music album."""
    album = {'artist_name': artist_name.title(
    ), 'album_title': album_title.title()}
    if number_songs:
        album['number_songs'] = number_songs
    return album


while True:
    print("\nEnter artist's name:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist's name: ")
    if a_name == 'q':
        break

    a_album = input("Album Title: ")
    if a_album == 'q':
        break

music1 = make_album(a_name, a_album)

# Messages
messages = ['hello', "I'll be right back", 'away from keyboard']
sent_messages = []


def show_messages(list1):
    """shows each text messages from the list"""
    for message in messages:
        print(message)


def send_messages(list1, list2):
    while list1:
        current_message = list1.pop()
        list2.append(current_message)


send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)

# Sandwiches


def make_sandwich(*sandwich_toppings):
    """Accepts a list of toppings a customer wants on their sandwich."""

    print(f"The following toppings are added to your sandwich:")
    for sandwich_topping in sandwich_toppings:
        print(f"\t- {sandwich_topping}")


make_sandwich('tomato', 'cheese', 'mayonaise', 'avocado', 'mustard')

# User Profile


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'jeffrey', 'lozano', gender='male', address='mandaluyong')
print(my_profile)

# Cars


def store_car_info(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info


my_car_info = store_car_info(
    'subaru', 'outback', color='blue', tow_package=True)
print(my_car_info)
