from pathlib import Path
from Functions import decryption_prepare_data
from Functions import encryption_key as encrypting

def decryption_procedure():
    print('-----------------------          \n'
          'How did you want load data?      \n'
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

    key = encrypting.make_reverse_dictionary(encrypting.make_encryption_dictionary(int(dict_message['seed']))) #  Generate key
    dict_message['length'] = decryption_prepare_data.len_decryption(dict_message['length']) #  Decode lenght

   # print('Message: ' + str(dict_message['message']))
    print(dict_message['length'])
    #print(decryption_prepare_data.split_data(dict_message['message'], dict_message['length']))