saldo = int(input("Informe o saldo: "))

if(saldo>=0 and saldo<=200):
  print("Seu saldo é de: {}, Nenhum credito foi liberado!" .format(saldo))
elif(saldo >= 201 and saldo <= 400):
  resultado = saldo * (20/100)
  print("Seu saldo médio é de: {}, credito no valor de: {}" .format(saldo,resultado))
elif(saldo >= 401 and saldo <= 600):
  resultado = saldo * (30/100)
  print("Seu saldo médio é de: {}, credito no valor de: {}" .format(saldo, resultado))
else:
  resultado = saldo * (40/100)
  print("Seu saldo médio é de: {}, credito no valor de: {}" .format(saldo, resultado))