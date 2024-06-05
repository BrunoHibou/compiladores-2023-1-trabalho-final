# Importa as funções do arquivo 'sintatico.py' e a biblioteca 're' (expressões regulares)
from sintatico import *
import re

# Função para ler o conteúdo de um arquivo removendo comentários
def ler_arquivo(teste):
    # Abre o arquivo no modo de leitura
    f = open(teste, 'r')
    program = ""  # Inicializa uma string para armazenar o conteúdo do programa
    buffer = ""  # Inicializa um buffer para armazenar temporariamente linhas de código
    state = "DEFAULT"  # Define o estado inicial como 'DEFAULT'
    in_multiline_comment = False  # Inicializa a flag indicando se está dentro de um comentário de bloco
    # Percorre todas as linhas do arquivo
    for line in f:
        i = 0
        # Percorre todos os caracteres de cada linha
        while i < len(line):
            if state == "DEFAULT":
                # Verifica se está dentro de um comentário de bloco
                if in_multiline_comment:
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                else:
                    # Verifica se encontrou um comentário de linha
                    if line[i:i + 2] == "//":
                        break
                    # Verifica se encontrou um comentário de bloco
                    elif line[i:i + 2] == "/*":
                        in_multiline_comment = True
                        i += 1
                    else:
                        program += line[i]  # Adiciona o caractere ao programa
            else:
                break
            i += 1

        if state == "DEFAULT":
            if not in_multiline_comment:
                program += buffer  # Adiciona o conteúdo do buffer ao programa
                buffer = ""  # Limpa o buffer

    f.close()  # Fecha o arquivo
    return program  # Retorna o conteúdo do programa

# Função para iniciar a análise léxica e sintática do programa
def iniciar_analisador(programa):
    programa = adicionar_espacos_delimitadores(programa)  # Adiciona espaços em torno de delimitadores
    programa = adicionar_espacos_operadores(programa)  # Adiciona espaços em torno de operadores
    print(programa)  # Imprime o programa com espaços adicionados
    print("\n----------------------------------------------------\n")
    tokens = tokenize(programa)  # Divide o programa em tokens
    print(tokens)  # Imprime os tokens
    parse(tokens)  # Inicia a análise sintática

# Função para dividir o programa em tokens
def tokenize(programa):
    tokens = []  # Inicializa uma lista para armazenar os tokens
    token_atual = ""  # Inicializa uma string para armazenar o token atual
    dentro_das_aspas = False  # Inicializa uma flag indicando se está dentro de aspas
    # Percorre todos os caracteres do programa
    for char in programa:
        if char == '"':
            if dentro_das_aspas:
                token_atual += char
                tokens.append(token_atual)
                token_atual = ""
                dentro_das_aspas = False
            else:
                if token_atual:
                    tokens.append(token_atual)
                    token_atual = ""
                dentro_das_aspas = True
                token_atual += char
        elif dentro_das_aspas:
            token_atual += char
        elif char.isspace():
            if token_atual:
                tokens.append(token_atual)
                token_atual = ""
        else:
            token_atual += char

    if token_atual:
        tokens.append(token_atual)

    return tokens  # Retorna a lista de tokens

# Função para adicionar espaços em torno de delimitadores
def adicionar_espacos_delimitadores(programa):
    padrao_aspas = r'"(.*?)"'  # Define um padrão para encontrar strings entre aspas
    ocorrencias = re.findall(padrao_aspas, programa)  # Encontra todas as strings entre aspas no programa
    marcador_espaco = "<ESPACO>"  # Define um marcador para espaços reservados
    espacos_reservados = []  # Inicializa uma lista para armazenar espaços reservados
    # Percorre todas as ocorrências de strings entre aspas
    for ocorrencia in ocorrencias:
        delimitador = f'"{ocorrencia}"'  # Cria um delimitador para a ocorrência
        # Substitui a ocorrência pelo delimitador com o marcador de espaço
        programa = programa.replace(delimitador, delimitador.replace(ocorrencia, marcador_espaco))
        espacos_reservados.append(ocorrencia)  # Adiciona a ocorrência à lista de espaços reservados

    # Adiciona espaços em torno de delimitadores
    programa = re.sub(r'[\(\)\[\]\{\};,:]', r' \g<0> ', programa)

    # Substitui os marcadores de espaço pelas ocorrências originais
    for espaco_reservado in espacos_reservados:
        programa = programa.replace(marcador_espaco, espaco_reservado, 1)

    return programa  # Retorna o programa com espaços adicionados

# Função para adicionar espaços em torno de operadores
def adicionar_espacos_operadores(programa):
    resultado = ''  # Inicializa uma string para armazenar o resultado
    entre_aspas = False  # Inicializa uma flag indicando se está dentro de aspas
    # Percorre todos os caracteres do programa
    for char in programa:
        if char == '"':
            entre_aspas = not entre_aspas  # Inverte o valor da flag
        # Verifica se está dentro de aspas
        if entre_aspas:
            resultado += char
        else:
            # Verifica se o caractere é um operador
            if char in operadores:
                resultado += ' ' + char + ' '  # Adiciona espaços em torno do operador
            else:
                resultado += char

    return resultado  # Retorna o programa com espaços adicionados
