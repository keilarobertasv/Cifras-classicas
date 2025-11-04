import numpy as np

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_MAP = {char: i for i, char in enumerate(ALFABETO)}
ALFA_MAP_INV = {i: char for i, char in enumerate(ALFA_MAP)}

def _mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def _algoritmo_euclidiano_ext(a, m):
    if _mcd(a, m) != 1:
        return None
    
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def _inverso_modular(det, m):
    return _algoritmo_euclidiano_ext(det % m, m)

def _matriz_inversa_modular(matriz, m):
    det = int(round(np.linalg.det(matriz)))
    det_inv = _inverso_modular(det, m)
    
    if det_inv is None:
        raise ValueError("A matriz da chave não é invertível. O determinante não é coprimo de 26.")
        
    matriz_adjunta = np.round(det * np.linalg.inv(matriz)).astype(int)
    matriz_inversa = (matriz_adjunta * det_inv) % m
    
    return matriz_inversa

def _validar_e_criar_chave(chave_str, m):
    if not chave_str:
        raise ValueError("A chave não pode estar vazia.")
    if m < 2:
        raise ValueError("O tamanho do bloco (m) deve ser >= 2.")
    
    numeros_str = chave_str.split()
    chave_nums = []
    
    try:
        for num_str in numeros_str:
            chave_nums.append(int(num_str))
    except ValueError:
        raise ValueError("A chave deve conter apenas números inteiros separados por espaço.")
            
    if len(chave_nums) != m * m:
        raise ValueError(f"A chave deve ter {m*m} números para um bloco de tamanho {m}.")
        
    matriz_chave = np.array(chave_nums).reshape(m, m)
    
    det = int(round(np.linalg.det(matriz_chave)))
    if det == 0:
        raise ValueError("A matriz da chave tem determinante zero, não é invertível.")
    if _mcd(det % 26, 26) != 1:
        raise ValueError("O determinante da matriz da chave não é coprimo de 26 (MDC != 1). Escolha outra chave.")
        
    return matriz_chave

def _preparar_texto(texto, m):
    texto_limpo = "".join(filter(str.isalpha, texto.upper()))
    
    padding_needed = (m - (len(texto_limpo) % m)) % m
    texto_limpo += "X" * padding_needed
    
    texto_vetores = []
    for i in range(0, len(texto_limpo), m):
        bloco = texto_limpo[i:i+m]
        vetor = [ALFA_MAP[char] for char in bloco]
        texto_vetores.append(np.array(vetor))
        
    return texto_vetores

def _vetores_para_texto(vetores):
    texto_final = ""
    for vetor in vetores:
        for num in vetor:
            texto_final += ALFA_MAP_INV[num % 26]
    return texto_final

def cifrar(texto, chave_str, m_str):
    try:
        m = int(m_str)
    except ValueError:
        raise ValueError("O tamanho do bloco (m) deve ser um número inteiro.")
        
    matriz_chave = _validar_e_criar_chave(chave_str, m)
    vetores_texto = _preparar_texto(texto, m)
    
    vetores_cifrados = []
    for vetor in vetores_texto:
        vetor_cifrado = np.dot(vetor, matriz_chave) % 26
        vetores_cifrados.append(vetor_cifrado)
        
    return _vetores_para_texto(vetores_cifrados)

def decifrar(texto, chave_str, m_str):
    try:
        m = int(m_str)
    except ValueError:
        raise ValueError("O tamanho do bloco (m) deve ser um número inteiro.")
        
    matriz_chave = _validar_e_criar_chave(chave_str, m)
    matriz_inversa = _matriz_inversa_modular(matriz_chave, 26)
    
    vetores_texto = _preparar_texto(texto, m)
    
    vetores_decifrados = []
    for vetor in vetores_texto:
        vetor_decifrado = np.dot(vetor, matriz_inversa) % 26
        vetores_decifrados.append(vetor_decifrado)
        
    return _vetores_para_texto(vetores_decifrados)