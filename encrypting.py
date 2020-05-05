def letter2num(message, key):
    if len(message) % 2 == 1:
        message += ' '

    out = []
    for letter in message:
        out.append(key[letter])
    return out


def num_multiplication(message):
    last2num = [None,None,None]
    multiplication_len = []
    multiplication_var = ''
    for index, num in enumerate(message):
        last2num[index % 2] = num
        if index % 2 == 1:
            if index % 4 == 1:
                last2num[2] = multiplication_and_key(last2num[0], last2num[1], last2num[0])
            elif index % 4 == 3:
                last2num[2] = multiplication_and_key(last2num[0], last2num[1], last2num[1])
            multiplication_len.append(len(last2num[2]))
            multiplication_var = multiplication_var + last2num[2]
    encrypted = {"encrypted_message": multiplication_var, "length": multiplication_len}
    return encrypted


def multiplication_and_key(first,second,key):
    return str(first*second)+str(key)

