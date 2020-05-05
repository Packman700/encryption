import polish_changer as pc  # My
import encryption_key  # My
import encrypting  # My
import pyperclip  # Copy

massage_to_encrypt = pc.change_polish_series(input('Enter massage to encrypt: ').lower())  # entering message
entered_seed = int(input('Enter seed: '))

###############
key = encryption_key.make_encryption_dictionary(entered_seed)  # make key

massage_to_encrypt = encrypting.letter2num(massage_to_encrypt, key)  # change letters to numbers
encrypted_message = encrypting.num_multiplication(massage_to_encrypt)  # using encryption method

encrypted_message['length'] = encrypting.len_encryption(encrypted_message['length'])  # encrypting len key

pyperclip.copy(str(encrypted_message['encrypted_message']) + ' ' + str(encrypted_message['length'])) # Copy to clipboard
spam = pyperclip.paste()  # Copy to clipboard

print('Massage copied to clipboard')