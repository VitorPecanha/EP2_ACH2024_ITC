"""
Aluno: Vitor Contieri Rezende Peçanha
Número USP: 10387706
"""

class Gramatica:
    def __init__(self, v1, t1, r1, regras):
        self.num_simbolos_n_termiais = v1
        self.num_simbolos_terminais = t1
        self.num_regras = r1
        self.simbolos_n_terminais = regras[0].split(' ')
        self.simbolos_terminais = regras[1].split(' ')
        self.simbolo_validos = self.simbolos_terminais + self.simbolos_n_terminais
        self.simbolo_validos.append('&')
        self.regras_substituicao = []
        self.erro = ''
    
        for i in range(2, len(regras)):
            aux = regras[i].split('=>')
            self.regras_substituicao.append(aux)

        for n_terminal in self.simbolos_n_terminais:
            if n_terminal in self.simbolos_terminais and self.erro == '':
                self.erro = 'ERRO 2'

        for terminal in self.simbolos_terminais:
            for i in range(self.num_regras):
                if terminal in self.regras_substituicao[i][0] and self.erro == '':
                    self.erro = 'ERRO 3'

        for i in range(self.num_regras):
            if len(self.regras_substituicao[i][0]) > 1:
                self.erro = 'ERRO 5'

def remove_vazio(gramaticas):
    for gramatica in gramaticas:
        novas_regras = []
        for i in range(gramatica.num_regras):
            if('&' in gramatica.regras_substituicao[i][1]):
                gramatica.num_regras -= 1
                continue
            novas_regras.append(gramatica.regras_substituicao[i])
        gramatica.regras_substituicao = novas_regras

def remove_unitaria(gramaticas):
    for gramatica in gramaticas:
        novas_regras = []
        for i in range(gramatica.num_regras):
            if(gramatica.regras_substituicao[i][0] in gramatica.regras_substituicao[i][1]):
                gramatica.num_regras -= 1
                continue
            novas_regras.append(gramatica.regras_substituicao[i])
        gramatica.regras_substituicao = novas_regras

def remove_inacessivel(gramaticas):
    for gramatica in gramaticas:
        acessiveis = []
        acessiveis.append(gramatica.regras_substituicao[0][0])
        for i in range(gramatica.num_simbolos_n_termiais):
            for j in range(gramatica.num_regras):
                if(gramatica.simbolos_n_terminais[i] in gramatica.regras_substituicao[j][1]) and (gramatica.simbolos_n_terminais[i] not in acessiveis):
                    acessiveis.append(gramatica.simbolos_n_terminais[i])
                    continue
        novas_regras = []
        for i in range(gramatica.num_regras):
            if(gramatica.regras_substituicao[i][0] not in acessiveis):
                gramatica.num_regras -= 1
                continue
            novas_regras.append(gramatica.regras_substituicao[i])
        gramatica.regras_substituicao = novas_regras

def escreve_gramaticas(gramaticas, saida):
    saida.write(str(len(gramaticas)) + '\n')
    for gramatica in gramaticas:
        if gramatica.erro != '':
            saida.write(gramatica.erro)
            continue
        saida.write(str(gramatica.num_simbolos_n_termiais) + ' ' + str(gramatica.num_simbolos_terminais) + ' ')
        saida.write(str(len(gramatica.regras_substituicao)) + '\n')
        for regras in gramatica.regras_substituicao:
            saida.write(regras[0] + ' => ' + regras[1])

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
for i in range(0, n):
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

    nova_gramatica = Gramatica(v1, t1, r1, regras)
    gramaticas.append(nova_gramatica)

remove_vazio(gramaticas)
remove_unitaria(gramaticas)
remove_inacessivel(gramaticas)
escreve_gramaticas(gramaticas, saida)

#fechando os arquivos
entrada.close()
saida.close()