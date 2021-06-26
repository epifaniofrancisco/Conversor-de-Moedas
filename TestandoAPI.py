while True:
    opcao = str(input("Quer converter? [S/N): ")).lower()

    if opcao == "s":

        while True:
            escolha = input("Converter para: ")

            if escolha.isnumeric():
                break
            else:
                print("\033[31mDIGITE APENAS NÚMEROS.\033[m")

        print("aceppt")
    else:
        break