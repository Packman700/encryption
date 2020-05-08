from pathlib import Path
from Functions import decryption
from Functions import encryption_key as encrypting
from Functions import encryption_key
import pyperclip  # Coping directory


def decryption_procedure():
    print('How did you want load data?      \n'
          '1.Paste                          \n'
          '2.File                            ')
    chose = str(input('Your chose: '))

    if chose == '1':  # Paste
        data = input('Enter text: ')

    elif chose == '2':  # File
        path = input('Enter the path: ')
        file_ex = Path(path)
        if file_ex.is_file():
            file = open(path, 'r')
            data = file.readline()

            file.close()
        else:
            print("File doesn't exist")
            exit()

    dict_message = decryption.prepare_data(data)  # Split data to 3 names

    #############
    while True:
        # Multiple decoding
        multiple_value = dict_message['seed'][-1:]
        dict_message['seed'] = dict_message['seed'][:-1]
        multiple_key = encryption_key.multiple_encryption_key(int(dict_message['seed']))

        key = encrypting.make_reverse_dictionary(
            encrypting.make_encryption_dictionary(int(dict_message['seed'])))  # Generate key

        len_key_temporary = encryption_key.len_encryption_dictionary(int(dict_message['seed']))  # Generate len key
        len_key = decryption.reverse_list_of_dictionary(len_key_temporary)  # Reverse len key

        dict_message['length'] = decryption.len_decryption(dict_message['length'], len_key)  # Decode lenght

        dict_message['message'] = decryption.split_data(dict_message['message'],
                                                        dict_message['length']['first'])  # split message

        dict_message['message'] = decryption.division_data(dict_message['message'],
                                                           dict_message['length']['second'])  # fist decode procedure
        decode_message = (decryption.key_decoding(dict_message['message'], key))  # key decode message

        if multiple_value in multiple_key['last_encrypting']:
            break
        else:
            dict_message = decryption.prepare_data(decode_message)

    ####################
    print('-----------------------')
    print('Decode message is: {}'.format(decode_message))
    pyperclip.copy(str(decode_message))  # Copy to clipboard
    spam = pyperclip.paste()
    print('Massage copied to clipboard')
    exit()
