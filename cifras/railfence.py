def _validar_chave(chave_str):
    try:
        chave = int(chave_str)
    except ValueError:
        raise ValueError("A chave (número de trilhos) deve ser um número inteiro.")
        
    if chave < 2:
        raise ValueError("A chave (número de trilhos) deve ser pelo menos 2.")
    
    return chave

def cifrar(texto, chave_str):
    chave = _validar_chave(chave_str)
    texto = "".join(filter(str.isalpha, texto.upper()))
    
    if chave >= len(texto):
        return texto

    trilhos = [''] * chave
    direcao = 1
    linha = 0

    for char in texto:
        trilhos[linha] += char
        linha += direcao
        
        if linha == 0 or linha == chave - 1:
            direcao = -direcao
            
    return "".join(trilhos)

def decifrar(texto_cifrado, chave_str):
    chave = _validar_chave(chave_str)
    texto_cifrado = "".join(filter(str.isalpha, texto_cifrado.upper()))
    
    if chave >= len(texto_cifrado):
        return texto_cifrado

    indices = list(range(len(texto_cifrado)))
    resultado_indices = [''] * len(texto_cifrado)
    
    trilhos_indices = [[] for _ in range(chave)]
    direcao = 1
    linha = 0

    for i in indices:
        trilhos_indices[linha].append(i)
        linha += direcao
        
        if linha == 0 or linha == chave - 1:
            direcao = -direcao
            
    idx_plano = []
    for trilho in trilhos_indices:
        idx_plano.extend(trilho)

    for i, idx in enumerate(idx_plano):
        resultado_indices[idx] = texto_cifrado[i]
        
    return "".join(resultado_indices)