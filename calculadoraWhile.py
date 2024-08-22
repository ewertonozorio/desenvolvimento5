def calculadora (opcao, num1, num2):
 
    if ((opcao <0) or (opcao>4)):
        return "Opa! Está opção não existe. Lei novamente as opções disponiveis"
    
    match opcao:
        case 1:
            resultado = num1+num2
        case 2:
            resultado = num1-num2
        case 3:
            resultado = num1*num2
        case 4:
            resultado = num1/num2
        case 0:
            return "Fim do programa"
    return resultado

while True:
    opcao = int(input("Escolha uma da opções: 0.Sair | 1.Soma | 2.Subtração | 3.Multiplicação | 4.Divisão: "))

    if opcao==0:
        print("Kbo o programa")
        break

    num1 = int(input("Entre com o valor do primeiro numero: "))
    num2 = int(input("Entre com o valor do segundo numero: "))

    resultado= calculadora(opcao, num1, num2)

    print(f"O resultado da sua operação é: {resultado}")