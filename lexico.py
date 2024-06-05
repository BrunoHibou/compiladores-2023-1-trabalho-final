# Importa todas as funções e classes do módulo 'dicionarios'.
from dicionarios import *
import re
import sys

# Função principal de análise léxica que processa um token.
def analisador_lexico(token):
    # Tenta encontrar constantes textuais no token.
    auxiliar = encontrar_constantes_textuais(token)
    if not auxiliar:
        # Se não encontrar, tenta encontrar palavras reservadas.
        auxiliar = encontrar_palavras_reservadas(token)
        if not auxiliar:
            # Se não encontrar, tenta encontrar operadores.
            auxiliar = encontrar_operadores(token)
            if not auxiliar:
                # Se não encontrar, tenta encontrar números.
                auxiliar = encontrar_numeros(token)
                if not auxiliar:
                    # Se não encontrar, tenta encontrar delimitadores.
                    auxiliar = encontrar_delimitadores(token)
                    if not auxiliar:
                        # Se não encontrar, tenta encontrar identificadores.
                        auxiliar = encontrar_identificadores(token)
                        if not auxiliar:
                            # Se não encontrar, reporta um erro léxico e encerra o programa.
                            print(f"erro lexico {token}")
                            sys.exit()
    
    return auxiliar

# Função para encontrar palavras reservadas no programa.
def encontrar_palavras_reservadas(programa):
    # Define um padrão regex para palavras reservadas.
    padrao = r"\b(" + "|".join(palavras_reservadas) + r")\b"
    palavras_reservadas_encontradas = re.findall(padrao, programa)
    return palavrasReservadas(palavras_reservadas_encontradas)

# Função para processar e retornar palavras reservadas encontradas.
def palavrasReservadas(palavras_reservadas_encontradas):
    if not palavras_reservadas_encontradas:
        return False
    for palavra in palavras_reservadas_encontradas:
        print(f"'{palavra}' é uma Palavra Reservada.")
        return palavra

# Função para encontrar operadores no programa.
def encontrar_operadores(programa):
    # Define um padrão regex para operadores.
    padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    operadores_encontrados = re.findall(padrao, programa)
    return retornar_operadores(operadores_encontrados)

# Função para processar e retornar operadores encontrados.
def retornar_operadores(operadores_encontrados):
    if not operadores_encontrados:
        return False
    for op in operadores_encontrados:
        print(f"'{op[1]}' é um Operador.")
        return op[1]

# Função para encontrar números no programa.
def encontrar_numeros(programa):
    # Verifica se há números com múltiplos pontos.
    encontrar_numeros_com_multiplos_pontos(programa)
    # Define um padrão regex para números.
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)
    inteiros = [num for num in numeros_encontrados if '.' not in num]
    floats = [num for num in numeros_encontrados if '.' in num]

    resposta = retornar_numeros(inteiros, 'Inteiro')
    if resposta:
        return resposta
    else:
        resposta = retornar_numeros(floats, 'Flutuante')

    return resposta

# Função para encontrar números com múltiplos pontos no programa.
def encontrar_numeros_com_multiplos_pontos(programa):
    count = 0
    for numero in programa:
        if numero == '.':
            count += 1
        if count > 1:
            print(f"Erro: número '{programa}' é inválido, pois tem múltiplos pontos.")
            sys.exit()

# Função para processar e retornar números encontrados.
def retornar_numeros(numeros, tipo):
    if not numeros:
        return False
    for num in numeros:
        print(f"'{num}' é um numeral {tipo}.")
        return "NUMBER"

# Função para encontrar constantes textuais no programa.
def encontrar_constantes_textuais(programa):
    # Define um padrão regex para constantes textuais.
    padrao = expressoes_regulares['constantes_textuais']
    constantes_encontradas = re.findall(padrao, programa)
    return retornar_constantes_textuais(constantes_encontradas)

# Função para processar e retornar constantes textuais encontradas.
def retornar_constantes_textuais(constantes_encontradas):
    if not constantes_encontradas:
        return False
    for constante in constantes_encontradas:
        print(f"'{constante}' é uma Constante Textual.")
        return "STRING"

# Função para encontrar delimitadores no programa.
def encontrar_delimitadores(programa):
    # Define um padrão regex para delimitadores.
    padrao = expressoes_regulares['delimitadores']
    delimitadores_encontrados = re.findall(padrao, programa)
    return retornar_delimitadores(delimitadores_encontrados)

# Função para processar e retornar delimitadores encontrados.
def retornar_delimitadores(delimitadores_encontrados):
    if not delimitadores_encontrados:
        return False
    for caracteres in delimitadores_encontrados:
        print(f"'{caracteres}' é um Delimitador.")
        return caracteres

# Função para encontrar identificadores no programa.
def encontrar_identificadores(programa):
    # Verifica caracteres não permitidos dentro de cada token.
    encontrar_caractere_nao_permitido(programa)
    # Verifica palavras com números.
    encontrar_palavras_com_numeros(programa)
    # Verifica palavras com pontos.
    encontrar_palavras_com_pontos(programa)
    # Define um padrão regex para identificadores.
    padrao = expressoes_regulares['identificadores']
    caracteres_identificadores = re.findall(padrao, programa)

    return retornar_identificadores(caracteres_identificadores)

# Função para processar e retornar identificadores encontrados.
def retornar_identificadores(identificadores_encontrados):
    if not identificadores_encontrados:
        return False
    for identificadores in identificadores_encontrados:
        print(f"'{identificadores}' é um identificador.")
        return "IDENTIFIER"

# Função para encontrar caracteres não permitidos no token.
def encontrar_caractere_nao_permitido(token):
    for caractere in token:
        if caractere not in ignoraveis and not any(re.findall(padrao, caractere) for padrao in expressoes_regulares.values()):
            print(f"Erro: o token '{token}' contém o caractere '{caractere}' que não é permitido!")
            sys.exit()

# Função para encontrar palavras que começam com números.
def encontrar_palavras_com_numeros(token):
    padrao = r'\b(\d+[a-zA-Z0-9_]*)\b'
    palavras_com_numeros = re.findall(padrao, token)
    for palavra in palavras_com_numeros:
        if re.match('^\d', palavra):
            print(f'Erro: "{palavra}" é uma palavra inválida pois começa com um número.')
            sys.exit()

# Função para encontrar palavras que contêm pontos.
def encontrar_palavras_com_pontos(token):
    for ponto in token:
        if ponto == '.':
            print(f"Erro: Identificador inválido com pontos no meio de caracteres: '{token}'")
            sys.exit()
