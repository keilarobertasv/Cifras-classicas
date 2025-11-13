import random
import string
import numpy as np
import math

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def _mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gerar_chave_cesar():
    return str(random.randint(1, 25))

def gerar_chave_monoalfabetica():
    lista_alfabeto = list(ALFABETO)
    random.shuffle(lista_alfabeto)
    return "".join(lista_alfabeto)

def gerar_chave_playfair():
    letras = list(string.ascii_uppercase)
    random.shuffle(letras)
    tamanho = random.randint(7, 10)
    return "".join(letras[:tamanho])

def gerar_chave_hill(m_str):
    try:
        m = int(m_str)
    except ValueError:
        raise ValueError("Tamanho do bloco 'm' deve ser um número.")
    if m < 2:
        raise ValueError("Tamanho do bloco 'm' deve ser >= 2.")
        
    tentativas = 0
    while tentativas < 1000:
        matriz = np.random.randint(0, 26, size=(m, m))
        det = int(round(np.linalg.det(matriz)))
        
        if det != 0 and _mcd(det % 26, 26) == 1:
            numeros = matriz.flatten()
            return " ".join(str(n) for n in numeros)
            
        tentativas += 1
        
    raise ValueError(f"Não foi possível gerar uma matriz invertível para m={m} após 1000 tentativas.")

def gerar_chave_vigenere():
    letras = string.ascii_uppercase
    tamanho = random.randint(5, 10)
    return "".join(random.choice(letras) for _ in range(tamanho))

def gerar_chave_vernam():
    letras = string.ascii_letters + string.digits
    tamanho = random.randint(8, 12)
    return "".join(random.choice(letras) for _ in range(tamanho))

def gerar_chave_otp(tamanho):
    if tamanho <= 0:
        raise ValueError("O texto não pode estar vazio para gerar uma chave OTP.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation + " "
    return "".join(random.choice(caracteres) for _ in range(tamanho))

def gerar_chave_railfence():
    return str(random.randint(2, 6))

def gerar_chave_colunar():
    letras = list(string.ascii_uppercase)
    random.shuffle(letras)
    tamanho = random.randint(5, 9)
    return "".join(letras[:tamanho])