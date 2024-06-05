from utils import *


def main():
    nome = './testes/teste1.ptc'
    programa = ler_arquivo(nome)  #retorna o programa a ser analisado sem comentários
    original = open(nome, 'r') #armazena o arquivo original 
    print(original.read())
    print("\n----------------------------------------------------\n")

    iniciar_analisador(programa) #analisa o programa sem comentários


if __name__ == "__main__":
    print("----------------- Análise Iniciada -----------------\n")
    main()
