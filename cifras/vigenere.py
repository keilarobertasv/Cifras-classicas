import string

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_MAP = {char: i for i, char in enumerate(ALFABETO)}
ALFA_MAP_INV = {i: char for i, char in enumerate(ALFA_MAP)}

def _validar_e_preparar_chave(chave_str):
    chave = "".join(filter(str.isalpha, chave_str.upper()))
    if not chave:
        raise ValueError("A chave não pode estar vazia e deve conter pelo menos uma letra.")
    
    chave_nums = [ALFA_MAP[char] for char in chave]
    return chave_nums

def _operacao_vigenere(texto, chave_str, modo):
    chave_nums = _validar_e_preparar_chave(chave_str)
    
    texto_processado = ""
    chave_idx = 0
    
    for char in texto.upper():
        if char in ALFA_MAP:
            texto_num = ALFA_MAP[char]
            chave_num = chave_nums[chave_idx % len(chave_nums)]
            
            if modo == 'cifrar':
                novo_num = (texto_num + chave_num) % 26
            else: 
                novo_num = (texto_num - chave_num) % 26
                
            texto_processado += ALFA_MAP_INV[novo_num]
            chave_idx += 1
        else:
            texto_processado += char
            
    return texto_processado

def cifrar(texto, chave_str):
    return _operacao_vigenere(texto, chave_str, 'cifrar')

def decifrar(texto, chave_str):
    return _operacao_vigenere(texto, chave_str, 'decifrar')