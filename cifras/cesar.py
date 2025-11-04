def _operacao_cesar(texto, chave):
    texto_processado = ""
    for char in texto.upper():
        if 'A' <= char <= 'Z':
            novo_codigo = (ord(char) - 65 + chave) % 26
            texto_processado += chr(novo_codigo + 65)
        else:
            texto_processado += char
    return texto_processado

def _validar_chave(chave_str):
    try:
        chave = int(chave_str)
    except ValueError:
        raise ValueError("A chave deve ser um número inteiro.")
        
    if not (1 <= chave <= 25):
        raise ValueError("A chave para a Cifra de César deve estar entre 1 e 25.")
    
    return chave

def cifrar(texto, chave_str):
    chave = _validar_chave(chave_str)
    return _operacao_cesar(texto, chave)

def decifrar(texto, chave_str):
    chave = _validar_chave(chave_str)
    return _operacao_cesar(texto, -chave)
