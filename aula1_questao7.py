import random

def encrypt(nomes):
    key = random.randint(1, 10)
    nomes_encriptados = []
    
    for nome in nomes:
        nome_encriptado = ""
        for letra in nome:
            if 33 <= ord(letra) <= 126:
                letra_encriptada = chr((ord(letra) - 33 + key) % 94 + 33)
                nome_encriptado += letra_encriptada
            else:
                nome_encriptado += letra
        nomes_encriptados.append(nome_encriptado)
    
    return nomes_encriptados, key

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_encriptados, chave_aleatoria = encrypt(nomes)
print("Nomes criptografados:", nomes_encriptados)
print("Chave aleatória:", chave_aleatoria)