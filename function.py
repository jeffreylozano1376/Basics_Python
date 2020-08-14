# Defining a Function
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Positional Arguments
describe_pet('harry', 'hamster')
# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')
# Default Value
describe_pet('willie')


# Return Values
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Optional Arguments
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# Returning a Dictionary / Optional Arguments
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 29)
print(musician)

# Passing a list to a function


def factory_make_product(product_list, completed_products):
    while product_list:
        current_product = product_list.pop()
        print(f"...Building {current_product.title()}...")
        completed_products.append(current_product)


def show_finished_product(completed_products):
    print("Construction complete:")
    for completed_model in completed_products:
        print(f"\t - {completed_model.title()}")


super_weapons = ['weather storm', 'nuclear weapon', 'psychic dominator']
basic_tanks = ['grizzly tank', 'rhino tank', 'lasher tank']

completed_super_weapons = []
completed_basic_tanks = []

# modifying a list in a function
factory_make_product(super_weapons, completed_super_weapons)
show_finished_product(completed_super_weapons)
# preventing modifying a list in a function (create list copy)
factory_make_product(basic_tanks[:], completed_basic_tanks)
show_finished_product(completed_basic_tanks)


# arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# arbitrary keyword arguments


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)
