from Functions import encryption_key


def prepare_data(data):
    split_message = data.split()
    dict_message = {
        'message': split_message[0],
        'length': split_message[1],
        'seed': split_message[2]
    }
    return dict_message


def len_decryption(length):
    out = []
    one_num = ''
    for index , character in enumerate(length):
        one_num = one_num + character
        if index % 7 == 6:
            out.append(encryption_key.key_encryption_dictionary[str(one_num)])
            one_num = ''
    return out


def split_data(data,len):
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


def division_data(data):
    out = []
    for index, number in enumerate(data):
        key_number = number[-2:]
        division_number = int(number[:-2])/int(key_number)
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

