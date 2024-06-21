from collections import Counter

print("Código para formar anagramas")
frase = input("Digite sua frase: ")
objetivo = input("Digite sua palavra objetivo: ")

def anagramas(x, y):
    p_final = []
    len_y = len(y)
    conta_y = Counter(y)
    espaco = Counter(x[:len_y])

    for i in range(len_y, len(x)):
        espaco[x[i]] += 1

        if espaco == conta_y:
            p_final.append(i - len_y + 1)
       
        espaco[x[i - len_y + 1]] -= 1
        if espaco[x[i - len_y + 1]] == 0:
            del espaco[x[i - len_y + 1]]

    return p_final

indices = anagramas(frase, objetivo)
print(f"Todos os anagramas: {indices}")