"""
Aluno: Vitor Contieri Rezende Peçanha
Número USP: 10387706
"""

class Gramatica:
    def __init__(self, r1, regras):
        self.simbolos_n_terminais = regras[0].split(' ')
        self.simbolos_terminais = regras[1].split(' ')
        self.regras_substituicao = []
    
        for i in range(2, r1):
            aux = regras[i].split('=>')
            self.regras_substituicao.append(aux)

#abertura do arquivo de entrada
entrada = open('entrada.txt', 'r')

#abertura do arquivo de saida
saida = open('saida.txt', 'a')

#lendo todas as linhas do arquivo
#e guardando em 'n' o número de gramáticas (primeiro elemento do arquivo)
linhas = entrada.readlines()
n = int(linhas[0])

if n < 0:
    saida.write('ERRO 1\n')
    quit()

gramaticas = []

posicao = 1
for i in range(0, int(n)):
    var = linhas[posicao].split()

    v1 = int(var[0])
    t1 = int(var[1])
    r1 = int(var[2])

    if v1 < 0 or t1 < 0 or r1 < 0:
        saida.write('ERRO 1\n')
        quit()

    aux = posicao + 1
    posicao = posicao + 3 + r1

    regras = []
    while aux < posicao:
        regras.append(linhas[aux])
        aux += 1

    nova_gramatica = Gramatica(r1, regras)
    gramaticas.append(nova_gramatica)

#fechando os arquivos
entrada.close()
saida.close()