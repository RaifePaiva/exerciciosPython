carbono = int(input("informe o conteúdo do carbono: "))
rokwell = int(input("Informe a dureza Rokwell: "))
resistencia = int(input("Informe a resistência a tração: "))

if carbono < 7 and rokwell > 50 and resistencia > 80000: 
    print("O grau do aço é 10, pois passou em todos os testes. ")
elif carbono < 7 and rokwell > 50 and resistencia < 80000: 
    print("O grau do aço é 9, pois passou apenas nos testes 1 e 2. ")
elif carbono < 7 and rokwell < 50 and resistencia < 80000: 
    print("O grau do aço é 8, pois passou apenas no teste 1. ")
elif carbono > 7 and rokwell < 50 and resistencia < 80000: 
    print("O grau do aço é 7")
