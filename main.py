import polish_changer as pc
import encryption_key


# Prepare massage
massage_to_encrypt = pc.change_polish_series(input('Enter massage to encrypt: ').lower())
entered_seed = int(input('Enter seed: '))

###############
key = encryption_key.make_encryption_dictionary(entered_seed)
print(key)

#aa