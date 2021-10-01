numero1 = int(input("Insira um numero para o calculo: "))
numero2 = int(input("Insira outro numero para o calculo: "))
print("Menu de calculos: Soma, Subtracao, Divisao, Multiplicacao, e Potencia")
escolha = input("Escolha o seu tipo de calculo: ")

def Soma(numero1, numero2):
    print(numero1 + numero2)

def Subtracao(numero1, numero2):
    print(numero1 - numero2)

def Divisao(numero1, numero2):
    print(numero1 / numero2)

def Multiplicacao(numero1, numero2):
    print(numero1 * numero2)

def Potencia(numero1, numero2):
    print(numero1 ** numero2)

if (escolha == "Soma"):
    Soma(numero1, numero2)
elif (escolha == "Subtracao"):
    Subtracao(numero1, numero2)
elif (escolha == "Divisao"):
    Divisao(numero1, numero2)
elif (escolha == "Multiplicacao"):
    Multiplicacao(numero1, numero2)
elif (escolha == "Potencia"):
    Potencia(numero1, numero2)

