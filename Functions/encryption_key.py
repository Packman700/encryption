import random
import math
import string


# This generate dictionary for all chars
def make_encryption_dictionary(seed):
    # Generate alphabet and numbers dictionary with 0 argument
    dictionary = dict.fromkeys(string.ascii_letters, 0)
    dictionary.update(dict.fromkeys(string.punctuation, 0))
    dictionary.update(dict.fromkeys(string.digits, 0))
    dictionary.update(dict.fromkeys(string.whitespace, 0))
    '''
    if True:  # This is just to organise code
        dictionary['!'] = 0
        dictionary['@'] = 0
        dictionary['#'] = 0
        dictionary['$'] = 0
        dictionary['%'] = 0
        dictionary['^'] = 0
        dictionary['&'] = 0
        dictionary['*'] = 0
        dictionary['('] = 0
        dictionary[')'] = 0
        dictionary['-'] = 0
        dictionary['_'] = 0
        dictionary['='] = 0
        dictionary['+'] = 0
        dictionary['{'] = 0
        dictionary['}'] = 0
        dictionary['['] = 0
        dictionary[']'] = 0
        dictionary['|'] = 0
        dictionary["\\"] = 0
        dictionary[':'] = 0
        dictionary[';'] = 0
        dictionary['"'] = 0
        dictionary["'"] = 0
        dictionary['<'] = 0
        dictionary['>'] = 0
        dictionary[','] = 0
        dictionary['.'] = 0
        dictionary['/'] = 0
        dictionary['?'] = 0
        dictionary['~'] = 0
        dictionary['`'] = 0
        dictionary[' '] = 0
    '''
    # Generate seed
    random.seed(math.sin(seed / 0.153) * -(1536 ** 2))  # random calculations

    # Generate unique value  for all chapter
    used_numbers = []
    for key in dictionary.keys():
        unique_value = False
        while not unique_value:
            test = random.randint(10, 999)
            if test not in used_numbers:
                unique_value = True

        used_numbers.append(test)
        dictionary[key] = used_numbers[-1]

    return dictionary


def make_reverse_dictionary(dictionary):
    out = {}
    for key, value in zip(dictionary.keys(), dictionary.values()):
        out[value] = key
    return out


#  This made len dictionary
def len_encryption_dictionary(seed):
    chars = dict.fromkeys(string.ascii_letters, 0)
    chars.update(dict.fromkeys(string.punctuation, 0))
    chars.update(dict.fromkeys(string.digits, 0))
    random.seed((seed-12)*123)

    used_numbers = []
    for key in chars.keys():
        unique_value = False
        while not unique_value:
            test = random.randint(0, len(chars)-1)
            if test not in used_numbers:
                unique_value = True
        used_numbers.append(test)
        chars[key] = used_numbers[-1]

    reverse_chars = make_reverse_dictionary(chars)
    len_key = {}
    used_values = []
    for index in range(2, 4):
        values_list = []
        for i in range(20):
            unique_value = False
            while not unique_value:
                test = reverse_chars[random.randint(0, len(chars)-1)] + reverse_chars[random.randint(0, len(chars)-1)]
                if test not in used_values:
                    unique_value = True
                    used_values.append(test)
                    values_list.append(test)
        len_key[index] = values_list
        del values_list

    for index in range(5, 10):
        values_list = []
        for i in range(20):
            unique_value = False
            while not unique_value:
                test = reverse_chars[random.randint(0, len(chars)-1)] + reverse_chars[random.randint(0, len(chars)-1)] + reverse_chars[random.randint(0, len(chars)-1)] + reverse_chars[random.randint(0, len(chars)-1)] + reverse_chars[random.randint(0, len(chars)-1)]
                if test not in used_values:
                    unique_value = True
                    used_values.append(test)
                    values_list.append(test)
        len_key[index] = values_list
        del values_list

    return len_key
