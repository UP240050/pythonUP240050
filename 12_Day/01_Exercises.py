#1.
import random
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    random_user = ''.join(random.choice(characters) for _ in range(6))
    return random_user
print ("User ID: ", generate_random_user_id())

#2.
def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for each user ID: "))
    num_ids = int(input("Enter the number of user IDs that you want: "))
    characters = string.ascii_letters + string.digits
    def random_user():
        return ''.join((random.choice(characters)) for _ in range(num_characters))
    for i in range(num_ids):
        random_id = random_user()
        print(f"{random_id}")
user_id_gen_by_user()

#3.
def rgb_color_gen():
    purple = random.randint(0,255)
    red =  random.randint(0,255)
    orange = random.randint(0,255)
    return(purple,red,orange)
random_rgb = rgb_color_gen ()
print(random_rgb)