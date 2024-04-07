#Após anlisar de novo as especificações do trabalho, acredito que os genes devam ser armazenados apenas
#em 0's e 1's... e nós estamos armazenando eles em 0's 1's .'s e ' ''s. 
#Aqui, irei corrigir isso.


#To fazendo uns testes nesse arquivo, testando a compatibilidade entre funções

#1 - Inicialização e mutação
        #UPDATE: Compatíveis
        
#2 - 

import random
import math

#def calculafit(pontosbinx,pontosbiny,t):
#    pontosdecx = [None] * t
#    pontosdecy = [None] * t
#    pontosdecz = [None] * t #cria listas para guardar os valores em decimal 
#    for i in range (t):
#        pontosdecx[i] = binario_para_float(pontosbinx[i]) #converte de binario para float r guarda num vetor
#        pontosdecy[i] = binario_para_float(pontosbiny[i]) #..
#        pontosdecz[i] = funcao(pontosdecx[i],pontosdecy[i]) #calcula o fitness da geração
#    return pontosdecz #retorna a lista com todos os fitness associados a cada índice de par (x,y)


def elitismo(listaGenes, listaElites, numElites):           #Recebe a população, e separa os X melhores indivíduos
    bestGene = 0
    for i in range(numElites):              #iteramos numElites vezes
        for j in range(len(listaGenes)):    #iteramos pela população
            #print("listaGenes[i][1] eh : ", listaGenes[i][1], " listaGenes[bestGene][1] eh: ", listaGenes[bestGene][1])
            if listaGenes[j][1] > listaGenes[bestGene][1]:  #encontramos o melhor gene
                #print("Trocamos! ", i)
                bestGene = j                #e armazenamos ele em bestGene

        listaElites.append(listaGenes.pop(bestGene)) #Removemos o melhor gene da população, colocamos ele na listaElites



def fitness(gene):                                      #Recebe um gene, separa o X do Y, retorna o fitness
    #essa função:
    #   Recebe uma string binária de 16 bits (gene)
    #   Separa o X do Y
    #   Converte eles em float
    #   Retornar o valor do fitness (funcao(X, Y))
    
    #Aqui, cortamos o gene pela metade:
    geneX = gene[:round(len(gene)/2)]   #Primeira metade vai pra X
    #print("X = ", geneX)
    geneY = gene[round(len(gene)/2):]   #Segunda metade vai pra Y
    #print("Y = ", geneY)
    
    #print("Float de X é =", binario_para_float(geneX))
    #print("Float de Y é =", binario_para_float(geneY))
    
    return funcao(binario_para_float(geneX), binario_para_float(geneY)) #Convertemos X e Y para Float, e calculamos o Z



def fitness_populacao(listaGenes):                      #Recebe a população, calcula todos os fitnesses
    #Recebe a matriz da população 
    #Pega os genes em [x][0]
    #Preenche os fitness em [x][1]
    
    for i in range(len(listaGenes)): #iteramos pelas linhas da matriz
        listaGenes[i][1] = fitness(listaGenes[i][0])
        


def print_lista(lista):                                 #Recebe uma lista e printa ela
    for i in lista: #printamos a lista
        print(i)



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
                
        geracao1.append([numero, fitness(numero)]) #colocamos nosso gene no final da lista



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



#Nota: Essa função inicializa a lista e já calcula o fitness automaticamente
def mutacao_populacao(populacao, taxa):                 #Muta toda a população da lista
    for i in range(len(populacao)):
        populacao[i][0] = mutacao_gene(populacao[i][0], taxa)   #Mutamos cada gene
        populacao[i][1] = fitness(populacao[i][0])              #E já calculamos se novo fitness



def float_para_binario(numero):                         #Recebe valor float, retorna string em binário ponto fixo
    if numero > 2.5:
        return "01010000"
    if numero < -2.5:
        return "11010000"
    casas = 5
    sinal_bit = '0' if numero >= 0 else '1' #quarda se o numero é positivo ou negativo
    numero = abs(numero)  # valor absoluto do número, mais fácil pra fazer a lógica do que tratar numeros positivos ou negativos
    

    parte_inteira = int(numero) #transforma o numero em inteiro
    
    parte_decimal = numero - parte_inteira #subtrai a parte inteira para separar a parte decimal
    
    binario_inteiro = bin(parte_inteira)[2:]  # usa a função bin pra transformar a parte inteira em string binária, e tira o prefixo 0b

    # Converter a parte fracionária para binário com precisão
    binario_decimal = []
    for _ in range(casas):
        parte_decimal *= 2
        bit = int(parte_decimal)          #logica de autoria do chatgpt
        binario_decimal.append(str(bit))
        parte_decimal -= bit
    
    if len(binario_inteiro) < 2:
            binario_inteiro = '0' + binario_inteiro #se a parte inteira tiver menos caracteres que 2, adicionar um 0 para manter 3 bits de cada lado

    binario_representacao = binario_inteiro + ''.join(binario_decimal) #soma as strings para juntar o inteiro e decimal
    
    binario_representatacao_sinal = sinal_bit + binario_representacao
    
    return binario_representatacao_sinal



def binario_para_float(partes):                         #Recebe string binaria ponto fixo, retorna valor float
   
    #bit_sinal = string_binaria[0]    # Verifica o bit de sinal e seta aflag de positivo ou negativo
    #e_negativo = True if bit_sinal == '1' else False
    e_negativo = bool(int(partes[0])) #Troquei por essa linha bem serelepe
        
    #partes = string_binaria[1:].split('.') # separa a parte inteira e a parte fracionária da string binária e guarda em vetor partes
    parte_inteira = partes[:3]
    parte_decimal = partes[3:]

    if parte_inteira == "100" and parte_decimal == "00000": 
        parte_inteira = "000"   #tratar 0 negativo
        e_negativo = False
        

    parte_inteira = parte_inteira[1:] #Essa linha serve para arrumar um bug que tava acontecendo antes
                                        #Basicamente, ele também convertia o primeiro bit (bit de sinal) para decimal
                                        #logo, todo número negativo acabava ficando menor que -4 (100)
                                        #E todo número negativo acabava sendo arredondado para -2.5    
   
    parte_inteira_float = int(parte_inteira, 2) #converte a parte inteira binaria pra inteiro decimal 
                                                #o 2 representa que o input está em binario
    
    parte_decimal_float = 0.0 #converte a parte fracionaria da string binária para fracionária decimal
                                #aqui eu percebi que toda vez que eu escrevi decimal até agora eu quis dizer fracionaria, mas fiquei com preguiça de mudar
    if len(parte_decimal) > 0:
        for i in range(len(parte_decimal)):
            bit_valor = int(parte_decimal[i])
            parte_decimal_float += bit_valor * (2 ** -(i + 1))  # logica de autoria do chatgpt
    
    resultado_float = parte_inteira_float + parte_decimal_float #soma as duas partes para chegar no valor final
     
    if e_negativo:
        resultado_float = -resultado_float #aplica sinal se a string binaria era negativa
    
    if resultado_float > 2.5:
        resultado_float = 2.5
    if resultado_float < -2.5:
        resultado_float = -2.5
    return resultado_float



def funcao(x,y):                                        #Recebe X e Y, retorna Z
    z = (pow(x,5)) - (10*(pow(x,3))) + (30*x) - (pow(y,2)) + (21*y)
    return z




#int main()
print("----- Algoritmo Genético -----")

#print("Testando float to bin")                     #FUNCIONAL
#while(True):
#    numeroF = float(input("Insira um float . : "))
#    numeroB = float_para_binario(numeroF)
#    print("Seu equivalente binário é: ", numeroB)
#    numeroF = binario_para_foat(numeroB)
#    print("E float de novo fica: ", numeroB)

#print("Testando bin to float")                     #FUNCIONAL
#while(True):
#    numeroB = input("Insira um bin . : ")
#    numeroF = binario_para_float(numeroB)
#    print("Seu equivalente float é: ", numeroF)
#    numeroB = float_para_binario(numeroF)
#    print("E bin de novo fica: ", numeroB)

#print("Testando f(x, y)")                          #FUNCIONAL
#while(True):
#    X = float(input("Insira X: "))
#    Y = float(input("Insira Y: "))
#    print("Z = ", funcao(X, Y))

#print("Testando fitness")                          #FUNCIONAL
#while(True):
#    gene = input("Insira um gene 16 bit: ")
#    print("Z = ", fitness(gene))



debug = input("Usar valores genéricos? (Menos tempo gasto debugando) (1 - Sim | 2 - Não): ")

if(debug == "2" or debug == "Não"):
    tamPopulacao = int(input("Insira o tamanho da população inicial (int): "))          #Pegamos o dado e convertemos em int
    tamGene      = int(input("Insira o tamanho dos genes (int) (recomendado - 16): "))  #(8 bits para X + 8 bits para Y)
    geracoes     = int(input("Insira o número máximo de gerações (int): "))
    taxaMutacao  = float(input("Insira a taxa de mutação (entre 0.01 e 0.05): "))       #Interpretado como relação (porcentagem/100)
    taxaElitismo = float(input("Insira a porcentagem de elitismo (recomendado - 0.5): "))      #Interpretado como porcentagem (%)
else:
    tamPopulacao = 10
    tamGene      = 16
    geracoes     = 5
    taxaMutacao  = 0.05
    taxaElitismo = 0.5


taxaElitismo = taxaElitismo / 100                           #Transformamos a porcentagem no seu equivalente numérico
taxaElitismo = int(math.ceil(taxaElitismo * tamPopulacao))  #Obtemos o valor absoluto de elites por geração


listaGenes  = []    #Matriz. Col 0 - Gene | Col 1 - Fitness
listaElites = []    #Matriz que armazena temporariamente genes removidos da listaGenes na função elitismo()


inicializa_genes(tamPopulacao, tamGene, listaGenes) #incializamos a função com os parâmetros acima
print("Sua pop inicial em binario é:")
print_lista(listaGenes)


for i in range(geracoes + 1):
    #fitness_populacao(listaGenes)  #Acho que essa função nem vai ser necessária,
                                    #já que o fitness sempre é recalculado logo quando um gene é alterado
    print("--------------------------------------------")
    print(" Nova iteração! Aqui está a lista de genes: ")
    print_lista(listaGenes)
    
    #Critério de parada aqui 
    if(i == (geracoes) or False): #Se alcançar o número máximo de iterações, ou outro criterio de parada lá
        i = geracoes + 8
        continue    #Termina o loop
    #-----------------

    #Elitismo aqui
    elitismo(listaGenes, listaElites, taxaElitismo)         #Obtemos os elites, inserimos eles na listaElites
    print("Temos ", taxaElitismo, " elites. Eles são: ")
    print_lista(listaElites)
    #-----------------
    
    #Seleção aqui
    #-----------------
    
    #cruzamento aqui
    #-----------------
    
    #Mutação aqui
    print("Agora vamos mutar  a lista")
    mutacao_populacao(listaGenes, taxaMutacao)
    print_lista(listaGenes)
    #-----------------
    
    #Aqui colocamos os elites de volta na listaGenes
    for i in range(len(listaElites)):           #iteramos pela listaElites
        listaGenes.append(listaElites.pop(i))   #Removemos os elites, e colocamos eles de volta na população
    #-----------------




#fitness_populacao(listaGenes)

#print("Sua pop mutada é:")
#print_lista(listaGenes)
