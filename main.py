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
n = linhas[0] if int(linhas[0]) >= 0 else saida.write('ERRO 1'), quit()

#for i in range(0, int(n)):


#fechando os arquivos
entrada.close()
saida.close()