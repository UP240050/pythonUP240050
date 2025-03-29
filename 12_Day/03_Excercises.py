import random

#1.
values =[10,11,12,13,14,15,16,171,8,19,20]
def shuffle_list(lst):
    random_lst = lst[:]
    random.shuffle(random_lst)
    return random_lst
print ("Original list: ", values)
print ("Random list: ", shuffle_list(values))

#2.
def random_nums ():
    random_num_lst = set()
    while (len(random_num_lst)<7):
        random_num = random.choice("123456789")
        random_num_lst.add(random_num)
    return list (random_num_lst)
print (random_nums())