import os
from math import sqrt
# Limpa o terminal
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione enter para continuar...")
# Receber número
def ler_float(mensagem):
    while True:
        try:
            num = float(input(mensagem))
            return num
        
        except ValueError:
            print("\nErro: Digite apenas números.")
# Armazenar dois números
def ler_dois_numeros():
    x = ler_float("Digite o primeiro número: ")
    y = ler_float("Digite o segundo número: ")

    return x, y
# Operações
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def potencia(x, y):
    return x ** y
# Menu
def menu():
    while True:
        limpar()
        print("===== Calculadora =====")
        print("[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão")
        print("[5] Potência\n[6] Raiz Quadrada\n[7] Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")

            pausar()
            continue

        if opcao == 1:
            print("\nSoma")

            num1, num2 = ler_dois_numeros()

            print("_________________________________\n")
            print(f"{num1} + {num2} = {soma(num1, num2):.2f}")

            pausar()
            continue

        elif opcao == 2:
            print("\nSubtração")

            num1, num2 = ler_dois_numeros()

            print("_________________________________\n")
            print(f"{num1} - {num2} = {subtracao(num1, num2):.2f}")

            pausar()
            continue

        elif opcao == 3:
            print("\nMultiplicação")

            num1, num2 = ler_dois_numeros()

            print("_________________________________\n")
            print(f"{num1} x {num2} = {multiplicacao(num1, num2):.2f}")

            pausar()
            continue

        elif opcao == 4:
            print("\nDivisão")

            num1, num2 = ler_dois_numeros()

            if num2 == 0:
                print("Erro: Divisão por zero")

                pausar()
                continue

            print("_________________________________\n")
            print(f"{num1} / {num2} = {divisao(num1, num2):.2f}")

            pausar()
            continue

        elif opcao == 5:
            print("\nPotência")

            num1, num2 = ler_dois_numeros()

            print("_________________________________\n")
            print(f"{num1}^{num2} = {potencia(num1, num2):.2f}")

            pausar()
            continue

        elif opcao == 6:
            print("\nRaiz quadrada")

            num = float(input("Digite o número: "))

            if num < 0:
                print("Erro: Número negativo.")

                pausar()
                continue

            print("_________________________________\n")
            print(f"√{num} = {sqrt(num):.2f}")

            pausar()
            continue

        elif opcao == 7:

            print("Fim do programa.\n")
            break

        else:
            print("Número inválido")

            pausar()