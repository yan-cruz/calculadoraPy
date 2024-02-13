import os
import time

operations = {
    "+": "Adição",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão", 
    "^": "Exponenciação"
}

welcome = 0

while True:
    os.system("cls")

    if welcome == 0:
        print("Bem-vindo à Caluladora!")
        print("")
        welcome += 1

    print("Operações disponíveis")

    i = 1
    for op, name in operations.items():    
        print(i, ":", name)
        i += 1

    print("")
    op = int(input("Digite a operação desejada: "))
    op_symbol = list(operations.keys())[op - 1]


    os.system("cls")
    print(">>> {} escolhida.".format(list(operations.values())[op - 1]))

    print("")
    num1 = float(input("Digite o 1º valor: "))
    num2 = float(input("Digite o 2º valor: "))

    if op == 1:
        result = num1 + num2
    elif op == 2:
        result = num1 - num2
    elif op == 3:
        result = num1 * num2
    elif op == 4:
        result = num1 / num2
    elif op == 5:
        result = num1 ** num2

    print("")
    print("{} {} {} = {}".format(num1, op_symbol, num2, result))

    print("")
    print("Deseja realizar outra operação?\n1 - Sim // 2 - Não")
    if float(input()) == 2:
        print("")
        print("Obrigado por utilizar a calculadora!")
        print("Desligando...")
        time.sleep(2)
        break