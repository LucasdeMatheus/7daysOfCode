numeroUm = 1
stringUm = '1'
numeroTrinta = 30
stringTrinta = '30'
numeroDez = 10
stringDez = '10'


#   em Python, uma string nunca será igual a um número, mesmo que representem o mesmo valor numérico.
#   'int()' transforma a string em inteiro
if numeroUm == int(stringUm):
    print('as variáveis numeroUm e stringUm tem o mesmo valor, mas tipos diferentes')
else:
    print('As variáveis numeroUm e stringUm não tem o mesmo valor')


#   tambem pode-se usa 'str()' para transformar um inteiro em string
if str(numeroDez) == stringDez:
    print('As variáveis numeroDez e stringDez tem o mesmo valor, mas tipos diferentes')
else:
    print('As variáveis numeroDez e stringDez não tem o mesmo valor')


#   o comparador 'is' compara apenas os tipos(string, int, float..)
if numeroTrinta is stringTrinta:
    print('As variáveis numeroTrinta e stringTrinta tem o mesmo valor e mesmo tipo')
else:
    print('As variáveis numeroTrinta e stringTrinta não tem o mesmo tipo')




