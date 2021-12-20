def check_prime(number):
    """ it's not best solution
    """
    special_non_numbers = [0, 1, 2]
    if number in special_non_numbers[:2]:
        return 2
    elif number == special_non_numbers[:-1]:
        return 3
    return all([number % i for i in range(2, number)])

def next_prime(value, factor=1, **kwargs):
    value = factor * value
    first_value_val = value

    while not check_prime(value)