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
    # This is just to organise code
    if True:
        dictionary['ą'] = 0
        dictionary['ć'] = 0
        dictionary['ę'] = 0
        dictionary['ł'] = 0
        dictionary['ń'] = 0
        dictionary['ó'] = 0
        dictionary['ś'] = 0
        dictionary['ż'] = 0
        dictionary['ź'] = 0
        dictionary['Ą'] = 0
        dictionary['Ć'] = 0
        dictionary['Ę'] = 0
        dictionary['Ł'] = 0
        dictionary['Ń'] = 0
        dictionary['Ó'] = 0
        dictionary['Ś'] = 0
        dictionary['Ż'] = 0
        dictionary['Ź'] = 0

    '''
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


# This generate key if you need multiple encrypt
def multiple_encryption_key(seed):
    # Generate list of chars
    chars = list(map(chr, range(59, 123))) + list(map(chr, range(33, 48)))
    random.seed(((seed + 777) ** 2) / 0.1943)
    # for safety
    x = random.randint(1, len(chars)-2)
    last_encrypting = [chars[x]]
    chars.pop(x)
    more_encrypting = [chars[x]]
    chars.pop(x)

    for char, in chars:
        if random.choice([True, False]):
            last_encrypting.append(char)
        else:
            more_encrypting.append(char)

    keys = {'last_encrypting':last_encrypting,'more_encrypting':more_encrypting}
    return keys


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
