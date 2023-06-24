import sys

aux = []
indentation = ""
traducao = ""
aux_elif = False


def iniciar_tradutor(string):
    global aux, indentation, traducao, aux_elif
    token = string[0]

    def decision():
        if aux:
            print("topo da lista auxiliar do tradutor: " + aux[-1])
        if aux[-1] == "print":
            escrever_print()
        elif aux[-1] == "fun":
            escrever_fun()
        elif aux[-1] == "var":
            escrever_var()
        elif aux[-1] == "while":
            escrever_while()
        elif aux[-1] == "if" or aux[-1] == "else" or aux[-1] == "elif":
            escrever_if_else_elif()
        else:
            escrever_programa()

    def escrever_print():
        global aux, traducao
        if token == ";":
            traducao = traducao + ")\n"
            aux.pop()
        elif token == "print":
            traducao = traducao + indentation + token + "("
        else:
            escrever_programa()

    def escrever_fun():
        global aux, indentation, traducao
        if token == "}":
            traducao = traducao + "\n"
            indentation = indentation[: -1]
            aux.pop()
        elif token == "{":
            traducao = traducao + ":" + "\n"
            indentation = indentation + " "
        elif token == "(":
            traducao = traducao + "("
        elif token == ")":
            traducao = traducao + ")"
        elif token == ";":
            traducao = traducao + "\n"
        elif token == "fun":
            traducao = traducao + "def "
        else:
            escrever_programa()

    def escrever_var():
        global aux, traducao
        if token == ";":
            traducao = traducao + "\n"
            aux.pop()
        elif token == "var":
            traducao = traducao + indentation + ""
        else:
            escrever_programa()

    def escrever_while():
        global aux, indentation, traducao
        if token == "}":
            traducao = traducao + "\n"
            indentation = indentation[: -1]
            aux.pop()
        elif token == "{":
            traducao = traducao + ":" + "\n"
            indentation = indentation + " "
        elif token == "(":
            traducao = traducao + " "
        elif token == ")":
            traducao = traducao + ""
        elif token == ";":
            traducao = traducao + "\n"
        else:
            escrever_programa()

    def escrever_if_else_elif():
        global aux, indentation, traducao, aux_elif
        print(aux[-1])
        if string[0] == "else" and string[1] == "if" and aux_elif:
            traducao = traducao + indentation + "elif" + " "
            aux.pop()
            print(aux_elif)
        elif token == "if" and aux_elif:
            aux_elif = False
        elif token == "if":
            print(aux_elif)
            traducao = traducao + indentation + token + " "
        elif token == "else":
            traducao = traducao + indentation + token + " "
        elif token == "}":
            traducao = traducao + "\n"
            indentation = indentation[: -1]
            aux.pop()
        elif token == "{":
            traducao = traducao + ":" + "\n"
            indentation = indentation + " "
        elif token == "(":
            traducao = traducao + " "
        elif token == ")":
            traducao = traducao + ""
        elif token == ";":
            traducao = traducao + "\n"
        else:
            escrever_programa()

    def escrever_programa():
        global aux, indentation, traducao
        if token == "}":
            print(f"--- SemanticError: Unexpected token '{token}'. ---")
            sys.exit()
        elif token == "{":
            print(f"--- SemanticError: Unexpected token '{token}'. ---")
            sys.exit()
        elif token == "(":
            traducao = traducao + "("
        elif token == ")":
            traducao = traducao + ")"
        elif token == ";":
            traducao = traducao + "\n"
        elif token == "!":
            traducao = traducao + "not"
        elif token == "true":
            traducao = traducao + "True"
        elif token == "false":
            traducao = traducao + "False"
        elif token == "nil":
            traducao = traducao + "None"
        else:
            traducao = traducao + indentation + token + " "

    def check():
        global aux_elif
        if token == "print":
            aux.append(token)
        elif token == "fun":
            aux.append(token)
        elif token == "var":
            aux.append(token)
        elif token == "while":
            aux.append(token)
        elif string[0] == "else" and string[1] == "if":
            aux.append("elif")
            aux_elif = True
        elif token == "if" and not aux_elif or token == "else" and not aux_elif:
            print(aux_elif)
            aux.append(token)

    check()

    if aux:
        decision()
    else:
        aux.append(token)
        decision()


def ler_programa():
    global traducao
    print(traducao)
    print("----------------- Executando o Código -----------------")
    exec(traducao)


'''

aux = []
indentation = ""


def iniciar_tradutor(string):
    global aux, indentation

    def decision():
        print("topo da lista auxiliar do tradutor: " + aux[-1])
        if aux[-1] == "print":
            escrever_print()
        elif aux[-1] == "fun":
            escrever_fun()
        elif aux[-1] == "var":
            escrever_var()
        elif aux[-1] == "while":
            escrever_while()
        elif aux[-1] == "if":
            escrever_if()
        else:
            escrever_programa()

    def escrever_print():
        global aux
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write("")
            if string == ";":
                arquivo.write(")\n")
                aux.pop()
            elif string == "print":
                arquivo.write(indentation + string + "(")
            else:
                escrever_programa()

    def escrever_fun():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write("")
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write("(")
            elif string == ")":
                arquivo.write(")")
            elif string == ";":
                arquivo.write("\n")
            elif string == "fun":
                arquivo.write("def ")
            else:
                escrever_programa()

    def escrever_var():
        global aux
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write("")
            if string == ";":
                arquivo.write("\n")
                aux.pop()
            elif string == "var":
                arquivo.write(indentation + "")
            else:
                escrever_programa()

    def escrever_while():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write("")
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write(" ")
            elif string == ")":
                arquivo.write("")
            elif string == ";":
                arquivo.write("\n")
            else:
                escrever_programa()

    def escrever_if():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write("")
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write(" ")
            elif string == ")":
                arquivo.write("")
            elif string == ";":
                arquivo.write("\n")
            else:
                escrever_programa()

    def escrever_programa():
        global aux, indentation
        with open("./testes/programa.py", "a") as arquivo:
            arquivo.write("")
            if string == "}":
                arquivo.write("\n")
                indentation = indentation[: -1]
                aux.pop()
            elif string == "{":
                arquivo.write(":" + "\n")
                indentation = indentation + " "
            elif string == "(":
                arquivo.write("(")
            elif string == ")":
                arquivo.write(")")
            elif string == ";":
                arquivo.write("\n")
            elif string == "!":
                arquivo.write("not")
            elif string == "true":
                arquivo.write("True")
            elif string == "false":
                arquivo.write("False")
            else:
                arquivo.write(indentation + string + " ")

    def check():
        if string == "print":
            aux.append(string)
        elif string == "fun":
            aux.append(string)
        elif string == "var":
            aux.append(string)
        elif string == "while":
            aux.append(string)
        elif string == "if":
            aux.append(string)

    check()

    if aux:
        decision()
    else:
        aux.append(string)
        decision()


def ler_programa():
    print(open("./testes/programa.py", "r").read())
    print("----------------- Executando o Código -----------------")
    exec(open("./testes/programa.py", 'r').read())


def apagar_txt(op):
    with open(op, 'w') as arquivo:
        arquivo.truncate()


'''
