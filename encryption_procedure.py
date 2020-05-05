from Functions import encryption_key, polish_changer as pc, encrypting
import pyperclip  # Coping directory


#  This is all what you need to encryption data
def encryption_procedure():
    #  Input data
    massage_to_encrypt = pc.change_polish_series(input('Enter massage to encrypt: ').lower())  # entering message
    entered_seed = int(input('Enter seed: '))

    #  Encrypting
    key = encryption_key.make_encryption_dictionary(entered_seed)  # make key
    print(key)

    massage_to_encrypt = encrypting.letter2num(massage_to_encrypt, key)  # change letters to numbers
    encrypted_message = encrypting.num_multiplication(massage_to_encrypt)  # using encryption method

    encrypted_message['length'] = encrypting.len_encryption(encrypted_message['length'])  # encrypting len key

    #  Saving
    print('----------------------- \n'
          'Where you want save?    \n'
          '1.Copy to clipboard     \n'
          '2.File                   ')
    chose = str(input('Your chose: '))

    if chose == '1':  # Copy to clipboard
        pyperclip.copy(
            str(encrypted_message['encrypted_message']) + ' ' + str(encrypted_message['length']) + ' ' + str(entered_seed))  # Copy to clipboard
        spam = pyperclip.paste()
        print('-----------------------')
        print('Massage copied to clipboard')

    elif chose == '2':  # File save
        result = open('Encryption.txt','w')
        result.write(str(encrypted_message['encrypted_message']) + ' ' + str(encrypted_message['length']) + ' ' + str(entered_seed))
        result.close()
        print('-----------------------')
        print('Successful save')