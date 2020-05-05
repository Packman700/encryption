d = {'1':'a','2':'b','3':'c','4':'d'}
a = '1234'
lista = []
'''''''''
for i, l in zip(range(len(a)),a):
    string = string + l
    if i%2:
        lista.append(string)
        string = ''
        '''''
for letter in a:
    lista.append(d[letter])
print (lista)