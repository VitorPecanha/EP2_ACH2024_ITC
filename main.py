"""
Aluno: Vitor Contieri Rezende Peçanha
Número USP: 10387706
"""

#abertura do arquivo de entrada
entrada = open('entrada.txt', 'r')

#abertura do arquivo de saida
saida = open('saida.txt', 'w')

#lendo todas as linhas do arquivo
#e guardando em 'n' o número de gramáticas (primeiro elemento do arquivo)
linhas = entrada.readlines()
n = linhas[0]

#fechando os arquivos
entrada.close()
saida.close()