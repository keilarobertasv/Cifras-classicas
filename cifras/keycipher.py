from .vigenere import cifrar as cifrar_vigenere, decifrar as decifrar_vigenere
from .vigenere import _validar_e_preparar_chave as _validar_chave_vigenere
from .transcolunas import cifrar as cifrar_colunar, decifrar as decifrar_colunar
from .transcolunas import _validar_chave as _validar_chave_colunar

def _validar_chaves(chave_vigenere_str, chave_colunar_str):
    if not chave_vigenere_str or not chave_colunar_str:
        raise ValueError("Ambas as chaves (Vigenère e Colunar) são obrigatórias.")
    
    _validar_chave_vigenere(chave_vigenere_str)
    _validar_chave_colunar(chave_colunar_str)
    
    return chave_vigenere_str, chave_colunar_str

def cifrar(texto, chave_vigenere_str, chave_colunar_str):
    chave_vig, chave_col = _validar_chaves(chave_vigenere_str, chave_colunar_str)
    
    texto_intermediario = cifrar_vigenere(texto, chave_vig)
    texto_cifrado = cifrar_colunar(texto_intermediario, chave_col)
    
    return texto_cifrado

def decifrar(texto_cifrado, chave_vigenere_str, chave_colunar_str):
    chave_vig, chave_col = _validar_chaves(chave_vigenere_str, chave_colunar_str)
    
    texto_intermediario = decifrar_colunar(texto_cifrado, chave_col)
    texto_decifrado = decifrar_vigenere(texto_intermediario, chave_vig)
    
    return texto_decifrado