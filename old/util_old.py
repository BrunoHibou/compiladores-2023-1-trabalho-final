from dict_old import *
import re
import sys


class Lexico:
    def __init__(self) -> None:
        self.element_list = []
        self.lista_de_tokens = []
        self.tabela_de_simbolos = []

        nome =  "/workspaces/Compilador-C/new/teste1.c"
        programa = self.ler_arquivo(nome)
        original = open(nome, 'r')
        print(original.read())


        rules = [self.find_text_constants, self.Find_reserved, self.find_ops, self.find_numbers, self.find_delimiters, self.find_identifiers]
        for rule in rules:
            programa = rule(programa)
            print('\n-----------------\n' + programa + '\n-----------------\n')

        print("------------------------------------ tokens ----------------------------------------------\n")
        for token in self.lista_de_tokens:
            print(token)
        print("----------------------------------- simbolos ---------------------------------------------\n")
        for symbol in self.tabela_de_simbolos:
            print(symbol)
        print("----------------------------------- tokens ---------------------------------------------\n")
        for element in self.element_list:
            print(element)

    def ler_arquivo(self, teste):
        f = open(teste, 'r')
        program = ""
        buffer = ""
        in_multiline_comment = False
        for line in f:
            i = 0
            while i < len(line):
                if in_multiline_comment:
                    # Estamos dentro de um comentário de bloco, ignoramos tudo até encontrar o final do comentário
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                else:
                    # Verifica se há um comentário de linha
                    if line[i:i + 2] == "//":
                        break  # ignoramos o restante da linha
                    elif line[i:i + 2] == "/*":
                        # Início do comentário de bloco
                        in_multiline_comment = True
                        i += 1
                    else:
                        program += line[i]  # Adicionamos o caractere à string do programa
                i += 1
            # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
            if not in_multiline_comment:
                program += buffer
                buffer = ""
        f.close()
        return program
    
    def analisador_lexico(self, token):
        auxiliar = self.find_text_constants(token)
        if not auxiliar:
            auxiliar = self.Find_reserved(token)
            if not auxiliar:
                auxiliar = self.find_ops(token)
                if not auxiliar:
                    auxiliar = self.find_numbers(token)
                    if not auxiliar:
                        auxiliar = self.find_delimiters(token)
                        if not auxiliar:
                            auxiliar = self.find_identifiers(token)
                            if not auxiliar:
                                print(f"erro lexico {token}")
                                sys.exit()
        return auxiliar


    def Find_reserved(self,programa):
        padrao = r"\b(" + "|".join(regex) + r")\b"
        regex_encontradas = re.findall(padrao, programa)
        return self.universal_printer(regex_encontradas, 'reserved word')

    def find_ops(self, programa):
        padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, ops))
        ops_encontrados = re.findall(padrao, programa)
        for index, value in enumerate(ops_encontrados):
            ops_encontrados[index] = ops_encontrados[index][1]
        return self.universal_printer(ops_encontrados, 'operator')
    def find_numbers(self, programa):
        self.find_multiple_floating_point_numbers(programa)

        padrao = regex['numerais']
        numeros_encontrados = re.findall(padrao, programa)
        
        inteiros = [num for num in numeros_encontrados if '.' not in num]
        self.universal_printer(inteiros, 'Integer')
        self.universal_printer(floats, 'Float')

        if inteiros:
            return inteiros
        floats = [num for num in numeros_encontrados if '.' in num]
        if floats:
            return floats

    def find_multiple_floating_point_numbers(self, programa):
        count = 0
        for numero in programa:
            if numero == '.':
                count +=1
            if count > 1:
                print(f"Erro: número '{programa}' é inválido, pois tem múltiplos pontos.")
                sys.exit()

    def find_text_constants(self,programa):
        padrao = regex['constantes_textuais']
        constantes_encontradas = re.findall(padrao, programa)
        return self.universal_printer(constantes_encontradas, 'text constant')

    def find_delimiters(self,programa):
        padrao = regex['delimitadores']
        delimitadores_encontrados = re.findall(padrao, programa)
        return self.universal_printer(delimitadores_encontrados, 'delimiter')

    def find_identifiers(self, programa):
        self.find_illegal_char(programa)
        self.find_alphanumerical(programa)
        self.find_words_with_dots(programa)
        padrao = regex['identificadores']
        caracteres_identificadores = re.findall(padrao, programa)

        return self.universal_printer(caracteres_identificadores, 'identifier')

    def find_illegal_char(self, programa):
        for caractere in programa:
            if caractere not in ops and caractere not in blank and not any(
                    re.findall(padrao, caractere) for padrao in regex.values()):
                print(f"Erro: o caractere '{caractere}' não é permitido!")
                sys.exit()

    def find_alphanumerical(self, programa):
        padrao = r'\b(\d+[a-zA-Z0-9_]*)\b'
        palavras_com_numeros = re.findall(padrao, programa)
        for palavra in palavras_com_numeros:
            if re.match('^\d', palavra):
                print(f'Erro: "{palavra}" é uma palavra inválida pois começa com um número.')
                sys.exit()

        return programa
    def find_words_with_dots(self, programa):
        for ponto in programa:
            if ponto == '.':
                print(f"Erro: Identificador inválido com pontos no meio de caracteres: '{programa}'")
                sys.exit()                     

    def universal_printer(self, list, type):
        if not list:
           print(f"None Found: {type}")
        for element in list:
            if type == 'identifier':
                if [element, type] not in self.tabela_de_simbolos:
                    self.tabela_de_simbolos.append([element, type])
            else:
                self.lista_de_tokens.append([element, type])
            self.element_list.append([element, type])