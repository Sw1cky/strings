numero = int(input("Digite seu numero de celular: "))

if len(numero) == 8:
    numero = "9" + numero

if len (numero) == 9 and numero[0] != "9":
    novo_numero = numero[:5] + "-" + numero[5:]

print("novo_numero", novo_numero)


      