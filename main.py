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
n = linhas[0] if int(linhas[0]) >= 0 else saida.write('ERRO 1\n')

posicao = 1

for i in range(0, int(n)):
    v1 = int(linhas[posicao][0])
    t1 = int(linhas[posicao][2])
    r1 = int(linhas[posicao][4])

    if v1 < 0 or t1 < 0 or r1 < 0:
        saida.write('ERRO 1\n')
        pass

    aux = posicao + 1
    posicao = posicao + 3 + r1

    regras = []
    while aux < posicao:
        regras.write(linhas[aux])
        aux += 1



#fechando os arquivos
entrada.close()
saida.close()