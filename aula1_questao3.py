frase = input("Digite sua frase: ")

numero_em_branco = 0 

for i in range(1, len(frase)):
    if frase[i] == " ":
     numero_em_branco += 1

print(f"O numero de espaços em branco é", numero_em_branco)