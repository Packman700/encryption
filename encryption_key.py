import random
import math
import string


def make_encryption_dictionary (seed):
    # Generate alphabet and numbers dictionary with 0 argument
    dictionary = dict.fromkeys(string.ascii_lowercase, 0)
    for x in range(10):
        dictionary[str(x)] = 0
    dictionary[' '] = 0

    # Generate seed
    random.seed(math.sin(seed / 0.153) * -(1536 ** 2))  # random calculations

    # Generate unique value  for all chapter
    used_numbers = []
    for key in dictionary.keys():
        unique_value = False
        while not unique_value:
            test = random.randint(10, 99)
            if test not in used_numbers:
                unique_value = True

        used_numbers.append(test)
        dictionary[key] = used_numbers[-1]

    return dictionary
