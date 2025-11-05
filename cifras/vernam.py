def _validar_chave(chave_str):
    if not chave_str:
        raise ValueError("A chave não pode estar vazia.")
    return chave_str

def _operacao_vernam_xor(texto, chave_str):
    chave = _validar_chave(chave_str)
    
    texto_bytes = texto.encode('utf-8')
    chave_bytes = chave.encode('utf-8')
    
    texto_cifrado_bytes = bytearray()
    
    for i in range(len(texto_bytes)):
        byte_texto = texto_bytes[i]
        byte_chave = chave_bytes[i % len(chave_bytes)]
        
        byte_cifrado = byte_texto ^ byte_chave
        texto_cifrado_bytes.append(byte_cifrado)
        
    try:
        return texto_cifrado_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return texto_cifrado_bytes.hex()

def cifrar(texto, chave_str):
    return _operacao_vernam_xor(texto, chave_str)

def decifrar(texto_cifrado, chave_str):
    chave = _validar_chave(chave_str)
    chave_bytes = chave.encode('utf-8')
    
    try:
        if all(c in '0123456789abcdefABCDEF' for c in texto_cifrado):
            texto_cifrado_bytes = bytearray.fromhex(texto_cifrado)
        else:
            texto_cifrado_bytes = texto_cifrado.encode('utf-8')
    except (ValueError, UnicodeEncodeError):
        texto_cifrado_bytes = texto_cifrado.encode('utf-8')

    texto_decifrado_bytes = bytearray()
    
    for i in range(len(texto_cifrado_bytes)):
        byte_cifrado = texto_cifrado_bytes[i]
        byte_chave = chave_bytes[i % len(chave_bytes)]
        
        byte_decifrado = byte_cifrado ^ byte_chave
        texto_decifrado_bytes.append(byte_decifrado)
        
    try:
        return texto_decifrado_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return "Erro: Não foi possível decodificar o resultado para texto. A chave pode estar incorreta."