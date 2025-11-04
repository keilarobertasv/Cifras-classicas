import string

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def _validar_chave(chave_str):
    chave = chave_str.upper()

    
    if len(chave) != 26:
        raise ValueError(f"A chave deve conter exatamente 26 letras. A sua tem {len(chave)}.")
    
    if len(set(chave)) != 26:
        raise ValueError("A chave não pode ter letras repetidas.")
    
    for char in chave:
        if char not in ALFABETO:
            raise ValueError(f"A chave contém caractere(s) inválido(s): '{char}'. Use apenas o alfabeto A-Z.")
    
    return chave

def cifrar(texto, chave_str):
    chave = _validar_chave(chave_str)
    mapa = str.maketrans(ALFABETO, chave)
    return texto.upper().translate(mapa)

def decifrar(texto, chave_str):
    chave = _validar_chave(chave_str)
    mapa = str.maketrans(chave, ALFABETO)
    return texto.upper().translate(mapa)