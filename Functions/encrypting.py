from Functions import encryption_key
import random


#  Convert pair letters to number
def letter2num(message, key):
    if len(message) % 2 == 1:
        message += ' '

    out = []
    for letter in message:
        out.append(key[letter])
    return out


#  This make directory with encrypted data section and unencrypted len part
def num_multiplication(message):
    last2num = [None, None, None]
    multiplication_len = []
    multiplication_var = ''
    for index, num in enumerate(message):
        last2num[index % 2] = num
        if index % 2 == 1:
            if index % 4 == 1:
                last2num[2] = multiplication_and_key(last2num[0], last2num[1], last2num[0])
            elif index % 4 == 3:
                last2num[2] = multiplication_and_key(last2num[0], last2num[1], last2num[1])
            multiplication_len.append(str(len(last2num[2])))
            multiplication_var = multiplication_var + last2num[2]
    encrypted = {"encrypted_message": multiplication_var, "length": multiplication_len}
    return encrypted


#  Converting len part with static key
def len_encryption(length):
    out = ''
    for char in length:
        out = out + encryption_key.key_encryption_dictionary[char][random.randint(0, 19)]
    return out


def multiplication_and_key(first,second,key):
    return str(first*second)+str(key)
