import string

def _limpar_chave(chave_str):
    chave = chave_str.upper().replace(" ", "")
    chave_limpa = ""
    for char in chave:
        if char not in chave_limpa and char in string.ascii_uppercase:
            chave_limpa += char
    return chave_limpa

def _gerar_matriz(chave_str):
    chave_limpa = _limpar_chave(chave_str)
    
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    matriz = []
    
    for char in chave_limpa:
        if char == 'J':
            char = 'I'
        if char not in matriz:
            matriz.append(char)
            
    for char in alfabeto:
        if char not in matriz:
            matriz.append(char)
            
    matriz_5x5 = [matriz[i:i+5] for i in range(0, 25, 5)]
    return matriz_5x5

def _encontrar_posicao(matriz, char):
    if char == 'J':
        char = 'I'
    for r in range(5):
        for c in range(5):
            if matriz[r][c] == char:
                return r, c
    return -1, -1

def _preparar_texto(texto_str):
    texto = "".join(filter(str.isalpha, texto_str.upper())).replace('J', 'I')
    
    texto_preparado = ""
    i = 0
    while i < len(texto):
        if i == len(texto) - 1:
            texto_preparado += texto[i] + 'X'
            i += 1
        elif texto[i] == texto[i+1]:
            texto_preparado += texto[i] + 'X'
            i += 1
        else:
            texto_preparado += texto[i] + texto[i+1]
            i += 2
            
    return texto_preparado

def _operacao_playfair(texto, chave, modo):
    matriz = _gerar_matriz(chave)
    texto_preparado = _preparar_texto(texto)
    texto_final = ""
    
    if modo == 'decifrar':
        deslocamento = -1
    else:
        deslocamento = 1
        
    for i in range(0, len(texto_preparado), 2):
        l1, l2 = texto_preparado[i], texto_preparado[i+1]
        
        r1, c1 = _encontrar_posicao(matriz, l1)
        r2, c2 = _encontrar_posicao(matriz, l2)
        
        if r1 == r2:
            texto_final += matriz[r1][(c1 + deslocamento) % 5]
            texto_final += matriz[r2][(c2 + deslocamento) % 5]
        elif c1 == c2:
            texto_final += matriz[(r1 + deslocamento) % 5][c1]
            texto_final += matriz[(r2 + deslocamento) % 5][c2]
        else:
            texto_final += matriz[r1][c2]
            texto_final += matriz[r2][c1]
            
    return texto_final

def cifrar(texto, chave_str):
    if not chave_str:
        raise ValueError("A chave não pode estar vazia.")
    return _operacao_playfair(texto, chave_str, 'cifrar')

def decifrar(texto, chave_str):
    if not chave_str:
        raise ValueError("A chave não pode estar vazia.")
    return _operacao_playfair(texto, chave_str, 'decifrar')