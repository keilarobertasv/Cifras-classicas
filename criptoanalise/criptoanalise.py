import string

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def calcular_frequencia(texto):
    texto = texto.upper()
    total_letras = 0
    contagem = {char: 0 for char in ALFABETO}
    
    for char in texto:
        if char in ALFABETO:
            contagem[char] += 1
            total_letras += 1
    
    if total_letras == 0:
        frequencia_pct = contagem
    else:
        frequencia_pct = {char: (count / total_letras) * 100 for char, count in contagem.items()}
        
    return frequencia_pct, total_letras