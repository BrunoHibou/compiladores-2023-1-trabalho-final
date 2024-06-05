# Importa todas as funções e classes do módulo 'utils'.
from utils import *

# Função principal que será executada quando o script for rodado.
def main():
    # Define o caminho do arquivo que contém o programa a ser analisado.
    nome = './testes/teste8.ptc'
    
    # Lê o conteúdo do arquivo especificado e retorna o programa sem comentários.
    programa = ler_arquivo(nome)  # 'ler_arquivo' é uma função importada de 'utils'.
    
    # Abre o arquivo original em modo de leitura.
    original = open(nome, 'r') # Armazena o arquivo original.
    
    # Lê e imprime o conteúdo do arquivo original.
    print(original.read())
    print("\n----------------------------------------------------\n")
    
    # Inicia o analisador para processar o programa sem comentários.
    iniciar_analisador(programa)  # 'iniciar_analisador' é outra função importada de 'utils'.

# Verifica se o script está sendo executado diretamente (não importado como um módulo).
if __name__ == "__main__":
    # Imprime uma mensagem indicando o início da análise.
    print("----------------- Análise Iniciada -----------------\n")
    # Chama a função principal.
    main()
