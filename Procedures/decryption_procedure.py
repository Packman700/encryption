from pathlib import Path
from Functions import decryption_prepare_data
from Functions import encryption_key as encrypting
import pyperclip  # Coping directory


def decryption_procedure():
    print('How did you want load data?      \n'
          '1.Paste                          \n'
          '2.File                            ')
    chose = str(input('Your chose: '))

    if chose == '1':  # Paste
        data = input('Enter the path: ')

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
    # Encryption.txt
    dict_message = decryption_prepare_data.prepare_data(data)

    #############
    key = encrypting.make_reverse_dictionary(
        encrypting.make_encryption_dictionary(int(dict_message['seed'])))  # Generate key
    dict_message['length'] = decryption_prepare_data.len_decryption(dict_message['length'])  # Decode lenght

    dict_message['message'] = decryption_prepare_data.split_data(dict_message['message'],
                                                                 dict_message['length'])  # split message

    dict_message['message'] = decryption_prepare_data.division_data(dict_message['message'])  # fist decode procedure
    decode_message = (decryption_prepare_data.key_decoding(dict_message['message'], key))  # key decode message

    ####################
    print('-----------------------')
    print('Decode message is: {}'.format(decode_message))
    pyperclip.copy(str(decode_message))  # Copy to clipboard
    spam = pyperclip.paste()
    print('Massage copied to clipboard')
    exit()