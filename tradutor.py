import sys

aux = []
indentation = ""
traducao = ""
aux_elif = False


def iniciar_tradutor(string, tipo):
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
            traducao = traducao + "("
        elif token == ")":
            traducao = traducao + ")"
        elif token == ";":
            traducao = traducao + "\n"
        else:
            escrever_programa()


    def escrever_programa():
        global aux, indentation, traducao
        if token == "}":
            print(traducao)
            print(string)
            print(f"--- SemanticError: Unexpected token '{token}'. ---")
            sys.exit()
        elif token == "{":
            print(traducao)
            print(string)
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
    def escrever_id():
        global aux, traducao
        if token == "(":
            traducao = traducao + "("
        elif token == ")":
            print("aaa1")
            traducao = traducao + ")"
            aux.pop()
        elif token == ";" and aux[-2] == "print":
            print("aaa2")
            traducao = traducao + "\n"
            aux.pop()
        elif token == ";":
            print("aaa2")
            traducao = traducao + "\n"
            aux.pop()
        else:
            escrever_programa()
            
            
            
            
            
            

def iniciar_tradutor(string, tipo):
    global aux, indentation, traducao, aux_elif
    token = string[0]

    def decision():
        if aux:
            print("topo da lista auxiliar do tradutor: " + aux[-1])
        if aux[-1] == "IDENTIFIER" and aux[-2] != "fun":
            escrever_id()
        elif aux[-1] == "print":
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
            a = 0
        # traducao = traducao + " "
        elif token == ")":
            a = 0
        #  traducao = traducao + ""
        elif token == ";":
            traducao = traducao + "\n"
        else:
            escrever_programa()

    def escrever_id():
        global aux, traducao
        if token == "(":
            traducao = traducao + "("
        elif token == ")":
            print("aaa1")
            traducao = traducao + ")"
            aux.pop()
        elif token == ";" and aux[-2] == "print":
            print("aaa2")
            traducao = traducao + "\n"
            aux.pop()
        elif token == ";":
            print("aaa2")
            traducao = traducao + "\n"
            aux.pop()
        else:
            escrever_programa()

    def escrever_programa():
        global aux, indentation, traducao
        if token == "}":
            print(traducao)
            print(string)
            print(f"--- SemanticError: Unexpected token '{token}'. ---")
            sys.exit()
        elif token == "{":
            print(traducao)
            print(string)
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
        if tipo == "IDENTIFIER" and aux[-1] != "fun":
            aux.append("IDENTIFIER")
        elif token == "print":
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
'''
