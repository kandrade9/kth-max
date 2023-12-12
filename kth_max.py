import random

def kth_max(my_list):
    """Generates a random k-integer to return the kth max integer of my_list"""
    length = len(my_list)  # find length of list to determine proper range
    k = random.randint(1, length)  # generate random integer using length range
    my_list.sort()  # sorts the list in ascending order
    result = my_list[-k]
    print(f"{result} is the {k} max integer of the list")
    return result

test_list = [40, 35, 82, 14, 22, 66, 53, 33, 56, 17, -1, -34, -80, 72]
max_int = kth_max(test_list)
