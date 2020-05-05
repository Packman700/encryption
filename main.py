import polish_changer as pc
import encryption_key
import encrypting as enc

# Prepare massage
massage_to_encrypt = pc.change_polish_series(input('Enter massage to encrypt: ').lower())
entered_seed = int(input('Enter seed: '))

###############
key = encryption_key.make_encryption_dictionary(entered_seed)
massage_to_encrypt = enc.letter2num(massage_to_encrypt, key)
encrypted_message = enc.num_multiplication(massage_to_encrypt)
print(str(encrypted_message['encrypted_message']) + str(encrypted_message['length']))
