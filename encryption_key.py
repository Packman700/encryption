import random
import math
import string


def make_encryption_dictionary(seed):
    # Generate alphabet and numbers dictionary with 0 argument
    dictionary = dict.fromkeys(string.ascii_lowercase, 0)
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
        dictionary[' '] = 0

    # Generate seed
    random.seed(math.sin(seed / 0.153) * -(1536 ** 2))  # random calculations

    # Generate unique value  for all chapter
    used_numbers = []
    for key in dictionary.keys():
        unique_value = False
        while not unique_value:
            test = random.randint(10, 99)
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


key_encryption_dictionary = {
    '5': [',w?+ks]', 'Qv9ZxUl', 'M$2jL-#', '<s=W4Qg', 'hT/vQ}#',
          'A-(h,wG', '>Q-XTlG', 'u^H*wO1', '0vIIOQD', 'ugF]y1$',
          '.YJ)^1k', 'XM!SQYX', 'N%;%yYM', 'N^gIl>3', 'kd6wB*_',
          'G7^u\]M', '0k@%n;=', 'mdU}iA8', '4LBO:yK', 'Q%4ma9g'],
    ',w?+ks]': '5', 'Qv9ZxUl': '5', 'M$2jL-#': '5', '<s=W4Qg': '5',
    'hT/vQ}#': '5', 'A-(h,wG': '5', '>Q-XTlG': '5', 'u^H*wO1': '5',
    '0vIIOQD': '5', 'ugF]y1$': '5', '.YJ)^1k': '5', 'XM!SQYX': '5',
    'N%;%yYM': '5', 'N^gIl>3': '5', 'kd6wB*_': '5', 'G7^u\]M': '5',
    '0k@%n;=': '5', 'mdU}iA8': '5', '4LBO:yK': '5', 'Q%4ma9g': '5',

    '6': ['[RG[O_h', '-!5J7Bu', 'SO7[y!v', 'chZh99f', 'l+8DMth',
          '6a%or8)', 'Y@-=OpB', 'M*(;mmw', 'WWcH2Kb', '*DTb^WZ',
          '9vs>@;A', 'n$)JYzh', '?KS)e#y', 'iYYejM}', '^SqdNjp',
          '0MSin#*', '1%^J13:', 'K*NOXE-', 'v[nU]*1', 'Nz;B#Nb'],
    '[RG[O_h': '6', '-!5J7Bu': '6', 'SO7[y!v': '6', 'chZh99f': '6',
    'l+8DMth': '6', '6a%or8)': '6', 'Y@-=OpB': '6', 'M*(;mmw': '6',
    'WWcH2Kb': '6', '*DTb^WZ': '6', '9vs>@;A': '6', 'n$)JYzh': '6',
    '?KS)e#y': '6', 'iYYejM}': '6', '^SqdNjp': '6', '0MSin#*': '6',
    '1%^J13:': '6', 'K*NOXE-': '6', 'v[nU]*1': '6', 'Nz;B#Nb': '6'
}
