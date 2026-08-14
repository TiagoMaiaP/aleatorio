import sys

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo numero: "))
sinal = str(input("Digite o sinal desejado para a operacao. + para soma, - subtraçao, * multiplicaçao, / divisão:    "))
result = 0

match sinal:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case _:
        sys.exit("ERRO")

    
print(f"O resultado é: {result}")