import json
import random, string
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
image = [('file', ('test.png', open(BASE_DIR/'data/test.png', 'rb'), 'image/png'))]


def generate_random_user_info():
    names_json = open(BASE_DIR/'data/names.json')
    names_and_surnames = json.load(names_json)
    while True:
        first_name = random.choice(list(names_and_surnames["names"]))
        last_name = random.choice(list(names_and_surnames["surnames"]))
        username = first_name[0] + last_name + str(random.randrange(1, 990))
        if 6 <= len(username) <= 12:
            break
        else:
            first_name, last_name,username = None, None, None
            continue
    age = random.randrange(18, 100)
    email = ('testuser_' + username + '@gmail.com').lower()
    password = ''.join(
        random.choices(string.ascii_letters, k=10)) + str(random.randint(10**4, 10**5-1))
    phone_number = str(random.randint(10**9, 10**10-1))

    random_user_info = {
        'username': username, 'email': email, 'password': password, 'first_name': first_name,
        'last_name': last_name, 'age': age, 'phone_number': phone_number,
    }
    return random_user_info


def generate_random_food_section_info():
    name = "Section" + str(random.randint(10**4,10**5))
    ordering_priority = random.randint(1, 10**3)
    is_available = True
    payload = {"name": name, "ordering_priority": ordering_priority, "is_available": is_available}
    return payload


def generate_random_food_item_info():
    name = "FoodItem" + str(random.randint(1,10**3))
    ordering_priority = int(random.randint(1, 10 ** 3))
    price = float(round(random.uniform(1, 10**3), 2))
    is_available = True
    payload = {'name': name,
               'food_section': '',
               'ordering_priority': ordering_priority,
               'price': price,
               'image': image[0][1][0],
               'is_available': is_available
               }
    return payload

