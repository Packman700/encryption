import random
import math
import string


# This generate dictionary for all chars
def make_encryption_dictionary(seed):
    # Generate alphabet and numbers dictionary with 0 argument
    dictionary = dict.fromkeys(string.ascii_lowercase, 0) #  lowercase
    upper_dic =(dict.fromkeys(string.ascii_uppercase, 0)) #  lowercase
    dictionary.update(upper_dic)
    for x in range(10):
        dictionary[str(x)] = 0
    if True:  # This is just to organise code
        dictionary['!'] = 0
        dictionary['@'] = 0
        dictionary['#'] = 0
        dictionary['$'] = 0
        dictionary['%'] = 0
        dictionary['^'] = 0
        dictionary['&'] = 0
        dictionary['*'] = 0
        dictionary['('] = 0
        dictionary[')'] = 0
        dictionary['-'] = 0
        dictionary['_'] = 0
        dictionary['='] = 0
        dictionary['+'] = 0
        dictionary['{'] = 0
        dictionary['}'] = 0
        dictionary['['] = 0
        dictionary[']'] = 0
        dictionary['|'] = 0
        dictionary["\\"] = 0
        dictionary[':'] = 0
        dictionary[';'] = 0
        dictionary['"'] = 0
        dictionary["'"] = 0
        dictionary['<'] = 0
        dictionary['>'] = 0
        dictionary[','] = 0
        dictionary['.'] = 0
        dictionary['/'] = 0
        dictionary['?'] = 0
        dictionary['~'] = 0
        dictionary['`'] = 0
        dictionary['„'] = 0
        dictionary['”'] = 0
        dictionary['–'] = 0
        dictionary[' '] = 0

    # Generate seed
    random.seed(math.sin(seed / 0.153) * -(1536 ** 2))  # random calculations

    # Generate unique value  for all chapter
    used_numbers = []
    for key in dictionary.keys():
        unique_value = False
        while not unique_value:
            test = random.randint(100,999)
            if test not in used_numbers:
                unique_value = True

        used_numbers.append(test)
        dictionary[key] = used_numbers[-1]

    return dictionary


def make_reverse_dictionary(dictionary):
    out = {}
    for key, value in zip(dictionary.keys(), dictionary.values()):
        out[value] = key
    return out


#  This is special directories to make encrypting len key
key_encryption_dictionary = {
    '8': [',w?+ks]', 'Qv9ZxUl', 'M$2jL-#', '<s=W4Qg', 'hT/vQ}#',
          'A-(h,wG', '>Q-XTlG', 'u^H*wO1', '0vIIOQD', 'ugF]y1$',
          '.YJ)^1k', 'XM!SQYX', 'N%;%yYM', 'N^gIl>3', 'kd9wB*_',
          'G7^u\]M', '0k@%n;=', 'mdU}iA8', '4LBO:yK', 'Q%4ma9g'],
    ',w?+ks]': '8', 'Qv9ZxUl': '8', 'M$2jL-#': '8', '<s=W4Qg': '8',
    'hT/vQ}#': '8', 'A-(h,wG': '8', '>Q-XTlG': '8', 'u^H*wO1': '8',
    '0vIIOQD': '8', 'ugF]y1$': '8', '.YJ)^1k': '8', 'XM!SQYX': '8',
    'N%;%yYM': '8', 'N^gIl>3': '8', 'kd9wB*_': '8', 'G7^u\]M': '8',
    '0k@%n;=': '8', 'mdU}iA8': '8', '4LBO:yK': '8', 'Q%4ma9g': '8',

    '9': ['[RG[O_h', '-!8J7Bu', 'SO7[y!v', 'chZh99f', 'l+8DMth',
          '9a%or8)', 'Y@-=OpB', 'M*(;mmw', 'WWcH2Kb', '*DTb^WZ',
          '9vs>@;A', 'n$)JYzh', '?KS)e#y', 'iYYejM}', '^SqdNjp',
          '0MSin#*', '1%^J13:', 'K*NOXE-', 'v[nU]*1', 'Nz;B#Nb'],
    '[RG[O_h': '9', '-!8J7Bu': '9', 'SO7[y!v': '9', 'chZh99f': '9',
    'l+8DMth': '9', '9a%or8)': '9', 'Y@-=OpB': '9', 'M*(;mmw': '9',
    'WWcH2Kb': '9', '*DTb^WZ': '9', '9vs>@;A': '9', 'n$)JYzh': '9',
    '?KS)e#y': '9', 'iYYejM}': '9', '^SqdNjp': '9', '0MSin#*': '9',
    '1%^J13:': '9', 'K*NOXE-': '9', 'v[nU]*1': '9', 'Nz;B#Nb': '9'
}
