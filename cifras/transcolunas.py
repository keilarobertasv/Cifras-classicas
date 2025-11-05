import math

def _validar_chave(chave_str):
    chave = chave_str.upper()
    if not chave or not all(c.isalpha() for c in chave):
        raise ValueError("A chave deve ser uma palavra contendo apenas letras.")
    
    if len(set(chave)) != len(chave):
        raise ValueError("A chave não pode ter letras repetidas.")
        
    return chave

def _obter_ordem_chave(chave):
    ordem_numerica = sorted(range(len(chave)), key=lambda k: chave[k])
    ordem_mapeada = [0] * len(chave)
    for i, idx in enumerate(ordem_numerica):
        ordem_mapeada[idx] = i
    return ordem_mapeada

def cifrar(texto, chave_str):
    chave = _validar_chave(chave_str)
    ordem_chave = _obter_ordem_chave(chave)
    texto = "".join(filter(str.isalpha, texto.upper()))
    
    num_cols = len(chave)
    texto_cifrado = ""
    
    for i in range(num_cols):
        idx_col_atual = ordem_chave.index(i)
        
        ptr = idx_col_atual
        while ptr < len(texto):
            texto_cifrado += texto[ptr]
            ptr += num_cols
            
    return texto_cifrado

def decifrar(texto_cifrado, chave_str):
    chave = _validar_chave(chave_str)
    ordem_chave = _obter_ordem_chave(chave)
    texto_cifrado = "".join(filter(str.isalpha, texto_cifrado.upper()))
    
    num_cols = len(chave)
    num_linhas = math.ceil(len(texto_cifrado) / num_cols)
    num_celulas = num_cols * num_linhas
    
    num_celulas_excesso = num_celulas - len(texto_cifrado)
    num_cols_curtas = num_celulas_excesso
    
    texto_decifrado = [''] * len(texto_cifrado)
    
    idx_texto = 0
    idx_ordem_leitura = 0
    
    for i in range(num_cols):
        idx_col_atual = ordem_chave.index(idx_ordem_leitura)
        
        comprimento_col = num_linhas
        
        if idx_col_atual >= num_cols - num_cols_curtas:
            comprimento_col = num_linhas - 1

        for j in range(comprimento_col):
            ptr_decifrar = idx_col_atual + (j * num_cols)
            if ptr_decifrar < len(texto_cifrado):
                texto_decifrado[ptr_decifrar] = texto_cifrado[idx_texto]
                idx_texto += 1
                
        idx_ordem_leitura += 1
        
    return "".join(texto_decifrado)