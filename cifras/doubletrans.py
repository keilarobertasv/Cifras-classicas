from .transcolunas import cifrar as cifrar_colunar, decifrar as decifrar_colunar
from .transcolunas import _validar_chave as _validar_chave_colunar

def _validar_chaves(chave1_str, chave2_str):
    if not chave1_str or not chave2_str:
        raise ValueError("Ambas as chaves (Chave 1 e Chave 2) são obrigatórias.")
    
    chave1 = _validar_chave_colunar(chave1_str)
    chave2 = _validar_chave_colunar(chave2_str)
    return chave1, chave2

def cifrar(texto, chave1_str, chave2_str):
    chave1, chave2 = _validar_chaves(chave1_str, chave2_str)
    
    texto_intermediario = cifrar_colunar(texto, chave1)
    texto_cifrado = cifrar_colunar(texto_intermediario, chave2)
    
    return texto_cifrado

def decifrar(texto_cifrado, chave1_str, chave2_str):
    chave1, chave2 = _validar_chaves(chave1_str, chave2_str)
    
    texto_intermediario = decifrar_colunar(texto_cifrado, chave2)
    texto_decifrado = decifrar_colunar(texto_intermediario, chave1)
    
    return texto_decifrado