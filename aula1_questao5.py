frase = str(input("Digite sua frase: "))

def contar_vogais(frase):
    vogal = "aeiouAEIOU"
    conta_vogal = 0
    indice = []

    for i, letra in enumerate(frase):
        if letra in vogal:
            conta_vogal += 1
            indice.append(i)

    return conta_vogal, indice

numero_vogais, indice = contar_vogais(frase)

print(F"O numero de vogais na frase é: {numero_vogais}")
print(f"O indice das vogais: {indice}")
               