# Importa todas as funções e classes necessárias dos módulos 'lexico' e 'tradutor'.
from lexico import *
from tradutor import *
import sys

# Função principal de parsing que processa uma lista de tokens.
def parse(tokens):
    current_token = None
    auxiliar = None
    token_index = 0

    # Função para avançar para o próximo token na lista.
    def advance():
        nonlocal current_token, token_index, auxiliar
        if token_index < len(tokens):
            current_token = tokens[token_index]
            auxiliar = analisador_lexico(current_token)
        else:
            current_token = None

    # Função para verificar e consumir o token esperado.
    def match(expected_token):
        nonlocal current_token, auxiliar
        if auxiliar == expected_token:
            iniciar_tradutor(tokens)
            tokens.pop(0)
            advance()
        else:
            print(f"--- SyntaxError: Expected '{expected_token}', but found '{current_token}'. ---")
            sys.exit()

    # Função principal do programa que processa declarações.
    def program():
        while current_token is not None:
            declaration()

    # Função que processa declarações.
    def declaration():
        if current_token == "fun":
            funDecl()
        elif current_token == "var":
            varDecl()
        else:
            statement()

    # Função que processa declarações de funções.
    def funDecl():
        match("fun")
        function()

    # Função que processa uma função.
    def function():
        match("IDENTIFIER")
        match("(")
        if current_token != ")":
            parameters()
        match(")")
        block()

    # Função que processa parâmetros de uma função.
    def parameters():
        match("IDENTIFIER")
        while current_token == ",":
            match(",")
            match("IDENTIFIER")

    # Função que processa um bloco de código.
    def block():
        match("{")
        while current_token != "}":
            declaration()
        match("}")

    # Função que processa declarações de variáveis.
    def varDecl():
        match("var")
        match("IDENTIFIER")
        if current_token == "=":
            match("=")
            expression()
        match(";")

    # Função que processa uma instrução.
    def statement():
        nonlocal auxiliar
        if auxiliar == "IDENTIFIER":
            exprStmt()
        elif current_token == "for":
            forStmt()
        elif current_token == "if":
            ifStmt()
        elif current_token == "print":
            printStmt()
        elif current_token == "return":
            returnStmt()
        elif current_token == "while":
            whileStmt()
        elif current_token == "{":
            block()
        else:
            print(f"--- SyntaxError: Unexpected token '{current_token}' in statement. ---")
            sys.exit()

    # Função que processa uma instrução de expressão.
    def exprStmt():
        expression()
        match(";")

    # Função que processa uma instrução de laço for.
    def forStmt():
        match("for")
        match("(")
        if current_token == "var":
            varDecl()
        elif current_token == "exprStmt":
            exprStmt()
        elif current_token != ";":
            expression()
        match(";")
        if current_token != ";":
            expression()
        match(";")
        if current_token != ")":
            expression()
        match(")")
        statement()

    # Função que processa uma instrução condicional if.
    def ifStmt():
        match("if")
        match("(")
        expression()
        match(")")
        statement()
        if current_token == "else":
            match("else")
            statement()

    # Função que processa uma instrução de impressão.
    def printStmt():
        match("print")
        expression()
        match(";")

    # Função que processa uma instrução de retorno.
    def returnStmt():
        match("return")
        if current_token != ";":
            expression()
        match(";")

    # Função que processa uma instrução de laço while.
    def whileStmt():
        match("while")
        match("(")
        expression()
        match(")")
        statement()

    # Função que processa uma expressão.
    def expression():
        assignment()

    # Função que processa uma atribuição.
    def assignment():
        nonlocal auxiliar
        if auxiliar == "IDENTIFIER":
            match("IDENTIFIER")
            if current_token == "=":
                match("=")
                assignment()
            else:
                logic_or()
        else:
            logic_or()

    # Função que processa uma expressão lógica OR.
    def logic_or():
        logic_and()
        while current_token == "or":
            match("or")
            logic_and()

    # Função que processa uma expressão lógica AND.
    def logic_and():
        equality()
        while current_token == "and":
            match("and")
            equality()

    # Função que processa uma igualdade.
    def equality():
        comparison()
        while current_token in ["!=", "=="]:
            match(current_token)
            comparison()

    # Função que processa uma comparação.
    def comparison():
        term()
        while current_token in [">", ">=", "<", "<="]:
            match(current_token)
            term()

    # Função que processa um termo.
    def term():
        factor()
        while current_token in ["-", "+"]:
            match(current_token)
            factor()

    # Função que processa um fator.
    def factor():
        unary()
        while current_token in ["/", "*"]:
            match(current_token)
            unary()

    # Função que processa uma operação unária.
    def unary():
        if current_token in ["!", "-"]:
            match(current_token)
            unary()
        else:
            call()

    # Função que processa uma chamada de função ou método.
    def call():
        primary()
        while current_token in ["(", "."]:
            if current_token == "(":
                match("(")
                if current_token != ")":
                    arguments()
                match(")")
            elif current_token == ".":
                match(".")
                match("IDENTIFIER")

    # Função que processa um elemento primário (literal, identificador, etc.).
    def primary():
        nonlocal auxiliar
        if auxiliar in ["true", "false", "nil", "this", "NUMBER", "STRING", "IDENTIFIER"]:
            match(auxiliar)
        elif auxiliar == "(":
            match("(")
            expression()
            if current_token == ",":
                arguments()
            match(")")
        elif auxiliar == "super":
            match("super")
            match(".")
            match("IDENTIFIER")

    # Função que processa argumentos de uma chamada de função.
    def arguments():
        expression()
        while current_token == ",":
            match(",")
            expression()

    # Inicia o processamento de tokens.
    advance()
    program()

    # Verifica se há tokens restantes após o término do parsing.
    if current_token is not None:
        print(f"--- SyntaxError: Unexpected token '{current_token}' at the end of the program. ---")
        sys.exit()
    else:
        print(tokens)
        print("\n----------------- Análise Sintática Concluída com Sucesso, Traduzindo o código para Python -----------------\n")
        ler_programa()  # Função que lê e traduz o programa para Python.
