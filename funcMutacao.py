#Primeiro vamos especificar os genes.
#cadeias de 16 bits
#               1-8 : valor de X
#               9-16: valor de Y, onde:
#                   bit 1   : Sinal
#                   bit 2-3 : Parte Int
#                   bit 4-8 : Parte Float

#Agora, vamos especificar a função mutação:
#   2 variáveis de entrada: Gene (16 bits); Taxa de mutação (de 1% a 5%)
#   1 variável de saída   : Gene mutado
#   O código percorre o gene, aplicando a chance de mutação em cada bit. Se um bit for escolhido, ele é flipado

#def: definimos uma função

import random


def mutacao_gene(gene, taxa):                           #Mutação de apenas um gene
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


        
gene = "001.001"
taxa = 0.05
print(gene)
gene = mutacao_gene(gene, taxa)
print(gene)