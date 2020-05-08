from Functions import encryption_key


def prepare_data(data):
    split_message = data.split()
    dict_message = {
        'message': split_message[0],
        'length': split_message[1],
        'seed': split_message[2]
    }
    return dict_message


def len_decryption(length, len_key):  # Split and decode len
    first_part = []
    second_part = []
    one_num = ''
    for index, character in enumerate(length):
        one_num = one_num + character
        if index % 7 == 6:
            first_part.append(one_num[:5])
            second_part.append(one_num[-2:])
            one_num = ''

    decoded_first = []
    decoded_second = []

    for first, second in zip(first_part, second_part):
        decoded_first.append(len_key[first]) #
        decoded_second.append(len_key[second])
    dic = {'first': decoded_first, 'second': decoded_second}
    return dic


def split_data(data, len):
    data_list = []
    current_number = ''
    index = 0
    for number in data:
        index += 1
        current_number = str(current_number) + str(number)
        if index % int(len[0]) == 0:
            index = 0
            data_list.append(current_number)
            current_number = ''
            len.pop(0)
    return data_list


def division_data(data, len_list):
    out = []
    for index, (number, length) in enumerate(zip(data, len_list)):
        key_number = number[-(length):]
        division_number = int(number[:-(length)]) / int(key_number)
        if index % 2 == 0:
            out.append(int(key_number))
            out.append(division_number)
        else:
            out.append(division_number)
            out.append(int(key_number))
    return out


def key_decoding(data, key):
    out = ''
    for encryption_letter in data:
        out = str(out) + str(key[encryption_letter])
    return out


def reverse_list_of_dictionary(list_dictionary):
    len_key = {}
    for l_key, l_var_list in zip(list_dictionary.keys(), list_dictionary.values()):
        for l_var in l_var_list:
            len_key[l_var] = l_key
    return len_key


def test (a):
    print(a['first'])
    return 0
