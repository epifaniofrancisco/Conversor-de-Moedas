"""
    Mostrador de mensagens e informações sobre conversões.

"""


def branco(moeda):
    return "\033[1;97m{}\033[m".format(moeda)


def apresentacao():
    print("\n\t\t\t\t\t\t             \033[32m A C E D E \033[m"
          "\n\t\t\t\t\t\t| - - - - - - - - - - - - - - - -|"
          "\n\t\t\t\t\t\t           B E M  V I N D O      "
          "\n\t\t\t\t\t\t| - - - - - - - - - - - - - - - -|"
          "\n\t\t\t\t\t\t \033[32mC O N V E R S O R DE M O E D A S\033[m"
          "\n\t\t\t\t\t\t| - - - - - - - - || - - - - - - |"
          "\n\t\t\t\t\t\t|   M O E D A S   ||  O P Ç Ã O  |"
          "\n\t\t\t\t\t\t| - - - - - - - - || - - - - - - |"
          "\n\t\t\t\t\t\t|  KWANZA <-> KZ  ||      1      |"
          "\n\t\t\t\t\t\t|  EURO   <-> £   ||      2      |"
          "\n\t\t\t\t\t\t|  DOLAR  <-> USD ||      3      |"
          "\n\t\t\t\t\t\t|  REAIS  <-> RS  ||      4      |"
          "\n\t\t\t\t\t\t|  LIBRA  <-> LB  ||      5      |"
          "\n\t\t\t\t\t\t|  SAIR           ||      0      |"
          "\n\t\t\t\t\t\t| - - - - - - - - || - - - - - - |\n")

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
