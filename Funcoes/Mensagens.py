"""
    Mostrador de mensagens e informações sobre conversões.

"""


def branco(moeda):
    return "\033[1;97m{}\033[m".format(moeda)


def mensagens(x):
    if x == 1:
        print("\n| - - - - - - - - - - - - -|"
              "\n|   VOCÊ ESCOLHEU {}   |    "
              "\n| - - - - - - - - - - - - -|\n".format(branco("KWANZA")))

        print(" CONVERTER DE {} PARA:  ".format(branco("KWANZA")))
        print("|   OPÇÃO   ||  CONVERTER  |")
        print("| - - - - - || - - - - - - |")
        print("|     1     ||    EURO     |")
        print("|     2     ||    DOLAR    |")
        print("|     3     ||    REAIS    |")
        print("|     4     ||    LIBRAS   |")
        print("| - - - - - || - - - - - - |")

    if x == 2:
        print("\n| - - - - - - - - - - - - -|"
              "\n|   VOCÊ ESCOLHEU {}     |  "
              "\n| - - - - - - - - - - - - -|".format(branco("EURO")))

        print("   CONVERTER DE {} PARA:    ".format(branco("EURO")))
        print("|   OPÇÃO   ||  CONVERTER  |")
        print("| - - - - - || - - - - - - |")
        print("|     1     ||    KWANZA   |")
        print("|     2     ||    DOLAR    |")
        print("|     3     ||    REAIS    |")
        print("|     4     ||    LIBRAS   |")
        print("| - - - - - || - - - - - - |")

    if x == 3:
        print("\n| - - - - - - - - - - - - -|"
              "\n|   VOCÊ ESCOLHEU {}    |   "
              "\n| - - - - - - - - - - - - -|".format(branco("DOLAR")))

        print("   CONVERTER DE {} PARA: ".format(branco("DOLAR")))
        print("|   OPÇÃO   ||  CONVERTER  |")
        print("| - - - - - || - - - - - - |")
        print("|     1     ||    KWANZA   |")
        print("|     2     ||    EURO     |")
        print("|     3     ||    REAIS    |")
        print("|     4     ||    LIBRAS   |")
        print("| - - - - - || - - - - - - |")

    if x == 4:
        print("\n| - - - - - - - - - - - - -|"
              "\n|   VOCÊ ESCOLHEU {}    |"
              "\n| - - - - - - - - - - - - -|".format(branco("REAIS")))

        print("   CONVERTER DE {} PARA: ".format(branco("REAIS")))
        print("|   OPÇÃO   ||  CONVERTER  |")
        print("| - - - - - || - - - - - - |")
        print("|     1     ||    KWANZA   |")
        print("|     2     ||    EURO     |")
        print("|     3     ||    DOLAR    |")
        print("|     4     ||    LIBRAS   |")
        print("| - - - - - || - - - - - - |")

    if x == 5:
        print("\n| - - - - - - - - - - - - -|"
              "\n|   VOCÊ ESCOLHEU {}   |    "
              "\n| - - - - - - - - - - - - -|\n".format(branco("LIBRAS")))

        print("  CONVERTER DE {} PARA: ".format(branco("LIBRAS")))
        print("|   OPÇÃO   ||  CONVERTER  |")
        print("| - - - - - || - - - - - - |")
        print("|     1     ||    KWANZA   |")
        print("|     2     ||    EURO     |")
        print("|     3     ||    DOLAR    |")
        print("|     4     ||    REAIS    |")
        print("| - - - - - || - - - - - - |")

    if x == 6:
        print("\n| - - - - - - - - - - - - - - - - - -|"
              "\n|        VOCÊ ESCOLHEU BTC           |"
              "\n| - - - - - - - - - - - - - - - - - -|")
