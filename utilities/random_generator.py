import json
import random, string


def generate_random_user_info():
    names_json = open('src/data/names.json')
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


