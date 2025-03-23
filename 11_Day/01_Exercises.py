#1.
def add_two_numbers ():
    num_one = 5
    num_two = 7
    total = num_one + num_two
    print(total)
add_two_numbers()

#2.
def area_circle ():
    Pi = 3.14
    r = 5
    area = Pi * r**2
    print(area)
area_circle()

#3.
def add_all_numbers (*args):
    if all (isinstance(num,(int, float)) for num in args):
        return sum(args)
    else:
        return "Error: All the arguments need to be numbers."


res = add_all_numbers(2, 4, 6, 4.6)
print(res)
res_error = add_all_numbers(2, 4, "seis", 3.6)
print(res_error)

#4.
def convert_celsius_to_farenheit(celsius):
    farenheit = (celsius * 9/5)+32
    return farenheit
temp_c = 27
temp_f = convert_celsius_to_farenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")

#5.
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
         return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autum'
    else:
        return 'Invalid month.'

print(check_season('july'))
print(check_season('January'))
print(check_season('may'))

#6.
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("The x-coordinates cannot be the same; slope is undefined.")
    return (y2 - y1) / (x2 - x1)

slope = calculate_slope(1, 2, 3, 4)
print("The slope is:", slope)

#7.
import cmath 

def _solve_quadratic_eqn(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")

    discriminant = b**2 - 4*a*c

    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return (root1, root2)
a = 1
b = -3
c = 2
solutions = _solve_quadratic_eqn(a, b, c)
print(f"The solutions are: {solutions}")

#8.
def print_list(my_list):
    for item in my_list:
        print(item)

mix_list = [1, 6, 19, 'onion', 'january']
print_list(mix_list)

#9.
def reverse_list(arr):
    reversed_arr = []  
    for i in range(len(arr) - 1, -1, -1): 
        reversed_arr.append(arr[i])  
    return reversed_arr
original_array = [1, 2, 3, 4, 5]
reversed_array = reverse_list(original_array)
print(reversed_array)  

#10.
def capitalize_list_items(items):
    capitalized_items = [] 
    for item in items: 
        capitalized_items.append(item.capitalize())  
    return capitalized_items

original_list = ['apple', 'banana', 'cherry', 'watermelon']
capitalized_list = capitalize_list_items(original_list)
print(capitalized_list)  

#11.
def add_item(food_staff, item):
    food_staff.append(item)
    return food_staff

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

def add_item(my_list, item):
    my_list.append(item)
    return my_list
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#12.
def remove_item(food_staff, item):

    if item in food_staff:
        food_staff.remove(item)
    return food_staff
item_to_remove = "Milk"
updated_list = remove_item(food_staff, item_to_remove)
print(updated_list)  

#13.
def sum_of_numbers(n):

    if n < 1:
        return 0  
    return sum(range(1, n + 1))
print(sum_of_numbers(5))  
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

#14.
def sum_of_odds(n):

    if n < 1:
        return 0  
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

#15.
def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total