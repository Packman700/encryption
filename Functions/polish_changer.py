# This function using change_polish_character function and convert polish to english sentence
def change_polish_series(sentence):
    series = ''
    for letter in sentence:
        series += change_polish_character(letter)
    return series


def change_polish_character(character):
    if character == 'ą': return 'a'
    if character == 'ć': return 'c'
    if character == 'ę': return 'e'
    if character == 'ł': return 'l'
    if character == 'ń': return 'n'
    if character == 'ó': return 'o'
    if character == 'ś': return 's'
    if character == 'ż': return 'z'
    if character == 'ź': return 'z'
    if character == 'Ą': return 'A'
    if character == 'Ć': return 'C'
    if character == 'Ę': return 'E'
    if character == 'Ł': return 'L'
    if character == 'Ń': return 'N'
    if character == 'Ó': return 'O'
    if character == 'Ś': return 'S'
    if character == 'Ż': return 'Z'
    if character == 'Ź': return 'Z'

    return character
