""" Crie um programa que leia uma frase qualquer e diga se ela é Polidromo. Desconsiderando os espaços.
EX: APÓS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA
"""
frase = str(input('Digite uma frase: ')).strip().upper()  # Strip = tira os espaços Upper deixa a letra maiusculas
palavras = frase.split()  # split separa as palavras em lista
junto = ''.join(palavras)  # Join junta as palavras
inverso = ''
"""for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]"""
inverso = junto[::-1]
print('O inverso de \033[0;34m{}\033[0m é \033[0;33m{}\033[0m'.format(junto, inverso))
if inverso == junto:
    print('\033[0;32mTemos um palíndromo!')
else:
    print('\033[31mA frase digítada não é um palíndromo!')
