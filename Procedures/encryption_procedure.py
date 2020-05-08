from Functions import encryption_key, polish_changer as pc, encrypting
import pyperclip  # Coping directory
import random


#  This is all what you need to encryption data
def encryption_procedure():
    #  Input data
    massage_to_encrypt = (input('Enter massage to encrypt: '))  # entering message
    how_many_encrypt = (input('How many time you want encrypt: '))

    #  Encrypting
    for index in range(int(how_many_encrypt)):
        entered_seed = random.randint(-100000000, 100000000)
        multiple_key = encrypting.chose_multiple_key(encryption_key.multiple_encryption_key(entered_seed), index)

        key = encryption_key.make_encryption_dictionary(entered_seed)  # make key

        massage_to_encrypt = encrypting.letter2num(massage_to_encrypt, key)  # change letters to numbers
        encrypted_message = encrypting.num_multiplication(massage_to_encrypt)  # using encryption method

        len_dic = encryption_key.len_encryption_dictionary(entered_seed)  # create key for len

        encrypted_message['length'] = encrypting.len_encryption(encrypted_message['length'], encrypted_message['key_length'], len_dic)  # encrypting len key
        massage_to_encrypt = str(encrypted_message['encrypted_message']) + ' ' + str(encrypted_message['length']) + ' ' + str(entered_seed) + str(multiple_key)

    #  Saving
    print('----------------------- \n'
          'Where you want save?    \n'
          '1.Copy to clipboard     \n'
          '2.File                   ')
    chose = str(input('Your chose: '))

    if chose == '1':  # Copy to clipboard
        pyperclip.copy(massage_to_encrypt)  # Copy to clipboard
        spam = pyperclip.paste()
        print('-----------------------')
        print('Massage copied to clipboard')
        exit()

    elif chose == '2':  # File save
        result = open('Encryption.txt','w')
        result.write(massage_to_encrypt)
        result.close()
        print('-----------------------')
        print('Successful save')
        exit()