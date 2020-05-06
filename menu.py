from Procedures import decryption_procedure, encryption_procedure
import os

print('     ENCRYPTION APP     \n'
      '----------------------- \n'
      'Chose operation:        \n'
      '1.Encryption            \n'
      '2.Decryption            ')
chose = str(input('Your chose: '))
print('-----------------------')

if chose == '1':
    encryption_procedure.encryption_procedure()
elif chose == '2':
    decryption_procedure.decryption_procedure()
else:
    os.system('cls')
