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

def mutacao_gene(gene, taxa):
    #vamos tratar ele como se fosse uma string(?)
    #percorremos a string, aplicamos if(taxademutação == rand()): swicthbit() else dont
    #return gene
    newgene = "" #aparentemente, strings sao imutáveis no python. Logo, precisamos criar uma nova string com o novo gene.
    
    for i in gene:
        j = i
        if random.random() < taxa:
            newgene += "0" if i == "1" else "1"
        else:
            newgene += j
        
    return newgene

        
gene = "01100101"
taxa = 0.05
print(gene)
gene = mutacao_gene(gene, taxa)
print(gene)