#Gera aleatoriamente uma população de n indivíduos
#Llimites de (𝑥 ∈ [−2.5, 2.5]; 𝑦 ∈ [−2.5, 2.5]);

#aparentemente, no python, listas podem ser passadas de uma função para outra sem problemas (passagem por referência)
import random

#Nota: Essa função inicializa a lista e já calcula o fitness automaticamente
def inicializa_genes(tamPopulacao, tamGene, geracao1):  #Recebe a lista, inicializa ela com valores randômicos
    
    for i in range(tamPopulacao):
        #Primeiro, vamos criar uma string vazia para armazenar nosso numero binario
        numero = ""        
        
        #Depois, geramos seus bits
        
        for i in range(tamGene): 
            if(i != 2 and i != 10): numero += str(random.randint(0, 1))     #geramos '0' ou '1'
            else:
                #Essa coisa abaixo serve para evitar que a parte inteira do gene seja igual a 3 (111 ou 011)  
                if(len(numero) == 2):  #gene X
                    if (numero[1] == "1" and i == 2): numero += "0"
                    else: numero += str(random.randint(0, 1))                   #geramos '0' ou '1'
    
                if(len(numero) == 10): #gene Y
                    if(numero[9] == "1" and i == 10): numero += "0"
                    else: numero += str(random.randint(0, 1))                   #geramos '0' ou '1'
        
        geracao1.append([numero, 0, 0]) #colocamos nosso gene no final da lista
    
    #fitness_populacao(listaGenes) #Calcula os fitnesses e corrige os limites da função
                    #Seria mais eficiente calcular o fitness enquanto a lista é populada, mas daí teria que arrumar um jeito de corrigir os limites da função


#int main()
tamPopulacao = 100
tamGene = 16        #(8 bits para X + 8 bits para Y)
listaGenes = [] #definimos a lista aonde será armazenado cada indivíduo da geração (em binário)

inicializa_genes(tamPopulacao, tamGene, listaGenes) #incializamos a função com os parâmetros acima

print("Sua pop inicial é:")
for i in listaGenes: #printamos a lista
    print(i)