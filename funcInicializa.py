#Gera aleatoriamente uma população de n indivíduos
#Llimites de (𝑥 ∈ [−2.5, 2.5]; 𝑦 ∈ [−2.5, 2.5]);

#aparentemente, no python, listas podem ser passadas de uma função para outra sem problemas (passagem por referência)
import random

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


#int main()
tamPopulacao = 100
tamGene = 16        #(8 bits para X + 8 bits para Y)
listaGenes = [] #definimos a lista aonde será armazenado cada indivíduo da geração (em binário)

inicializa_genes(tamPopulacao, tamGene, listaGenes) #incializamos a função com os parâmetros acima

print("Sua pop inicial é:")
for i in listaGenes: #printamos a lista
    print(i)