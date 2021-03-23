"""
    Módulo usado para converter as moedas.

    - Kwanza
    - Euro
    - Dolar
    - Reais
    - Libras
"""

from Funcoes.Mensagens import mensagens

def conversor_kwanza():
    mensagens(1)

    valor = float(input("\nValor Kz: "))

    print("  ESCOLHA PARA CONVERTER KWANZA PARA: ")
    print("|        OPÇÃO      ||   CONVERTER   |")
    print("| - - - - - - - - - || - - - - - - - |")
    print("|          1        ||      EURO     |")
    print("|          2        ||      DOLAR    |")
    print("|          3        ||      REAIS    |")
    print("|          4        ||      LIBRAS   |")
    print("| - - - - - - - - - || - - - - - - - |")

    escolha = int(input("\nEscolha: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA EURO    |"
              "\n| - - - - - - - - - - - - |")

        print("{} Kz equivalem a {} Euros.".format(valor, valor * 1))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA DOLAR    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Kz equivalem a {} Dolares.".format(valor, valor * 1))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA REAIS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Kz equivalem a {} Reais.".format(valor, valor * 1))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    KWANZA PARA LIBRAS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Kz equivalem a {} Libras.".format(valor, valor * 1))


def conversor_euro():
    mensagens(2)

    valor = float(input("\nValor £: "))

    print("  ESCOLHA PARA CONVERTER EURO PARA: ")
    print("|        OPÇÃO      ||   CONVERTER   |")
    print("| - - - - - - - - - || - - - - - - - |")
    print("|          1        ||      KWANZA   |")
    print("|          2        ||      DOLAR    |")
    print("|          3        ||      REAIS    |")
    print("|          4        ||      LIBRAS   |")
    print("| - - - - - - - - - || - - - - - - - |")

    escolha = int(input("\nEscolha: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    EURO PARA KWANZA    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Kz.".format(valor, valor * 1))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    EURO PARA DOLAR      |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Dolares.".format(valor, valor * 1))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    EURO PARA REAIS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Reais.".format(valor, valor * 1))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    EURO PARA LIBRAS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Libras.".format(valor, valor * 1))


def conversor_dolar():
    mensagens(3)

    valor = float(input("\nValor USD: "))

    print("  ESCOLHA PARA CONVERTER DOLAR PARA: ")
    print("|        OPÇÃO      ||   CONVERTER   |")
    print("| - - - - - - - - - || - - - - - - - |")
    print("|          1        ||      KWANZA   |")
    print("|          2        ||      EURO    |")
    print("|          3        ||      REAIS    |")
    print("|          4        ||      LIBRAS   |")
    print("| - - - - - - - - - || - - - - - - - |")

    escolha = int(input("\nEscolha: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA KWANZA    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Kz.".format(valor, valor * 1))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA EURO      |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Euros.".format(valor, valor * 1))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA REAIS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Reais.".format(valor, valor * 1))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    DOLAR PARA LIBRAS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Dolares equivalem a {} Libras.".format(valor, valor * 1))


def conversor_reais():
    mensagens(4)

    valor = float(input("\nValor Rs: "))

    print("  ESCOLHA PARA CONVERTER REAIS PARA: ")
    print("|        OPÇÃO      ||   CONVERTER   |")
    print("| - - - - - - - - - || - - - - - - - |")
    print("|          1        ||      KWANZA   |")
    print("|          2        ||      EURO    |")
    print("|          3        ||      DOLAR    |")
    print("|          4        ||      LIBRAS   |")
    print("| - - - - - - - - - || - - - - - - - |")

    escolha = int(input("\nEscolha: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA KWANZA    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Kz.".format(valor, valor * 1))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA EURO      |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Euros.".format(valor, valor * 1))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA DOLAR    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Dolares.".format(valor, valor * 1))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    REAIS PARA LIBRAS    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Reais equivalem a {} Libras.".format(valor, valor * 1))


def conversor_lbras():
    mensagens(5)

    valor = float(input("\nValor LB: "))

    print("  ESCOLHA PARA CONVERTER LIBRAS PARA: ")
    print("|        OPÇÃO      ||   CONVERTER   |")
    print("| - - - - - - - - - || - - - - - - - |")
    print("|          1        ||      KWANZA   |")
    print("|          2        ||      EURO     |")
    print("|          3        ||      DOLAR    |")
    print("|          4        ||      REAIS    |")
    print("| - - - - - - - - - || - - - - - - - |")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA KWANZA   |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Libras equivalem a {} Kz.".format(valor, valor * 1))

    if escolha == 2:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA EURO     |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Libras equivalem a {} Euros.".format(valor, valor * 1))

    if escolha == 3:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA DOLAR    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Libras equivalem a {} Dolares.".format(valor, valor * 1))

    if escolha == 4:
        print("\n| - - - - - - - - - - - - |"
              "\n|    LIBRAS PARA Reais    |"
              "\n| - - - - - - - - - - - - |")

        print("\n{} Euros equivalem a {} Reais.".format(valor, valor * 1))