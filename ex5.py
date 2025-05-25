def inverte_string(s):
    invertida = ''
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

texto = "Teste Target"

resultado = inverte_string(texto)
print(f"{resultado}")