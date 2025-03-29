import random
import string

#1.
def list_of_hexa_colors(nums):
    hexa_co = []
    for _ in range(nums):
        random_color = '#' + ''.join(random.choices("0123456789abcdef",k=6))
        hexa_co.append(random_color)
    return hexa_co
print(list_of_hexa_colors(6))

#2.
def list_of_rgb_colors(num):
    lst_rgb_co = []
    for _ in range(num):
        purple = random.randint(0,255)
        red =  random.randint(0,255)
        orange = random.randint(0,255)
        lst_rgb_co.append(('rgb', purple,red,orange))
    return lst_rgb_co
print (list_of_rgb_colors(5))

#3.
def generate_colors(num, type):
    colors = []
    if type == 'hexa':
        for _ in range(num):
            rand_color = "#" + ''.join(random.choices("0123456789abcdef",k=6))
            colors.append(rand_color)
        return colors
    elif type == 'rgb':
        for _ in range(num):
            purple = random.randint(0,255)
            red =  random.randint(0,255)
            orange = random.randint(0,255)
            colors.append(('rgb', purple,red,orange))
        return colors
    else:
        print("Invalid color type")

print ("Generate Hexa colors: ", generate_colors("Hexa", 4))
print ("Generate RGB colors: ", generate_colors("RGB", 4))
print (generate_colors("tp", 5))