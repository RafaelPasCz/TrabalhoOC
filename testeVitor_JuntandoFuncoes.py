#To fazendo uns testes nesse arquivo, testando a compatibilidade entre funções

#1 - Inicialização e mutação
        #UPDATE: Compatíveis
        
#2 - 

import random

def print_lista(lista):
    for i in lista: #printamos a lista
        print(i)


def inicializa_genes(tamPopulacao, tamGene, geracao1): #recebe a lista por endereço
    for i in range(tamPopulacao):
        #Primeiro, vamos criar uma string vazia para armazenar nosso numero binario
        numero = ""
        #Depois, geramos seus bits
        for i in range(tamGene+2):
            if i == 3 or i == ((tamGene/2) + 4):
                numero += "."
            else:
                numero += str(random.randint(0, 1)) #geramos um int entre 0 e 1, e convertemos pra string
        geracao1.append(numero) #colocamos nosso gene no final da lista


def mutacao_gene(gene, taxa): #mutação de apenas um gene
    #Tratamo o gene como string
    newgene = "" #Strings são imutáveis no python. Logo, precisamos criar uma nova string com o novo gene.
    
    for i in gene: #Percorremos a string, e aplicamos a taxa de mutação
        if i == ".":
            newgene += "."
        else:
            if random.random() < taxa:
                newgene += "0" if i == "1" else "1"
            else:
                newgene += i
    return newgene


def mutacao_populacao(populacao, tamPopulacao, taxa):
    for i in range(tamPopulacao):
        populacao[i] = mutacao_gene(populacao[i], taxa)





#int main()
print("----- Algoritmo Genético -----")

tamPopulacao = int(input("Insira o tamanho da população inicial (int): "))          #Pegamos o dado e convertemos em int
tamGene      = int(input("Insira o tamanho dos genes (int) (recomendado - 16): "))  #(8 bits para X + 8 bits para Y)
taxaMutacao  = float(input("Insira a taxa de mutação (entre 0,01 e 0,05): "))

listaGenes = [] #definimos a lista aonde será armazenado cada indivíduo da geração (em binário)

inicializa_genes(tamPopulacao, tamGene, listaGenes) #incializamos a função com os parâmetros acima

print("Sua pop inicial é:")
print_lista(listaGenes)

print("Agora vamos mutar ela")

mutacao_populacao(listaGenes, tamPopulacao, taxaMutacao)

print("Sua pop mutada é:")
print_lista(listaGenes)
