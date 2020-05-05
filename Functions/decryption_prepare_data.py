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
    current_number = None
    for index, number in enumerate(data):
        current_number = current_number + number
        if index % len[0] == 0:
            data_list.append(current_number)
            current_number
            len.pop(0)