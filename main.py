"""
 ** Autor: Epifânio Francisco
 ** Data: 23/03/2021  Hora: 12:41
 ** Função: Converter moedas.
"""

from Funcoes.Mensagens import apresentacao
from Funcoes.Conversores import conversor_kwanza, conversor_euro, conversor_dolar, conversor_reais, conversor_libras

while True:
    while True:
        opcao = str(input("Quer converter? [S/N]: ")).lower()

        if opcao in "s" or opcao in "n":
            break
        else:
            print("\033[31mDIGITE APENAS S OU N.\033[m")

    if opcao == "s":
        apresentacao()

        while True:
            escolha = input("Escolha a moeda que vai converter: ")

            if escolha.isnumeric():
                if escolha in "012345":
                    escolha = int(escolha)
                    break
                else:
                    print("\033[31mDIGITE APENAS NÚMEROS PRESENTES NA TABELA ACIMA.\033[m")
            else:
                print("\033[31mDIGITE APENAS NÚMEROS.\033[m")

        if escolha == 1:
            conversor_kwanza()
        if escolha == 2:
            conversor_euro()
        if escolha == 3:
            conversor_dolar()
        if escolha == 4:
            conversor_reais()
        if escolha == 5:
            conversor_libras()

        if escolha == 0:
            break
    elif opcao == "n":
        break

print("\t\t\t\t\t\t\t\t | - - - - - - - - |")
print("\t\t\t\t\t\t\t\t | FIM DO PROGRAMA |")
print("\t\t\t\t\t\t\t\t | - - - - - - - - |")
print("\t\t\t\t\t\t\t\t\t \033[32m A C E D E \033[m")
print("\t\t\t\t\t\t\t\t | - - - - - - - - |")
