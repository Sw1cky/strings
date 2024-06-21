def validar_cpf(cpf):
   
    cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]
    if len(cpf_numeros) != 11:
        return False
    
    soma = sum((cpf_numeros[i] * (10 - i)) for i in range(9))
    resto = soma % 11
    verifica_digito1 = 0 if resto < 2 else 11 - resto

    if cpf_numeros[9] != verifica_digito1:
        return False
    
    soma = sum((cpf_numeros[i] * (11 - i)) for i in range(10))
    resto = soma % 11
    digito_verifica2 = 0 if resto < 2 else 11 - resto

    if cpf_numeros[10] != digito_verifica2:
        return False
    
    return True

cpf_usuario = input("Digite o CPF (no formato XXX.XXX.XXX-XX): ")
cpf_nao_formatado = ''.join(filter(str.isdigit, cpf_usuario))


if validar_cpf(cpf_nao_formatado):
    print("CPF válido.")
else:
    print("CPF inválido.")