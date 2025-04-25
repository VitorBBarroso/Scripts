n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while True:
    print("\nEscolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    alternativa = input("Digite o número da operação desejada: ")

    if alternativa == "1":
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} é {soma}")
    elif alternativa == "2":
        subtracao = n1 - n2
        print(f"A subtração de {n1} - {n2} é {subtracao}")
    elif alternativa == "3":
        multiplicacao = n1 * n2
        print(f"A multiplicação de {n1} * {n2} é {multiplicacao}")
    elif alternativa == "4":
        if n2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            divisao = n1 / n2
            print(f"A divisão de {n1} / {n2} é {divisao}")
    elif alternativa == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")