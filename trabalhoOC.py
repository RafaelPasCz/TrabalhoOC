#Poggers


import random
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.axes3d import Axes3D
import colorcet #Bibliotema com vários color maps bonitinhos
from matplotlib.gridspec import GridSpec
import names


def random_naonulo():
    while True:
        num = random.random()  # num é aleatório, onde: {0 < num < 1}
        if num != 0:
            return num

def fitnessMedio(listaGenes, listaFitness):                               #Recebe a população, calcula seu fitness médio
    fitnessMedio = 0.0 #Var que armazena o soma e a média dos fitnesses
    
    for i in listaGenes:
        fitnessMedio += i[1]    
        
    fitnessMedio = fitnessMedio/len(listaGenes)
    
    listaFitness.append(fitnessMedio) #Calculamos o fitness médio, colocamos ele na listaFitness
    
    
def criaGraficos(listaFitness, populacao, ax1, ax2, ax3, ax4, listaElites):
    listaFitnessAux = []
    
    for i in range(len(listaFitness)):
        listaFitnessAux.append(i)
    
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    
    fig.clear()
    
    
    #Plotagem do gráfico do fitness médio por geração
    
    #plt.subplot(2, 1, 1)
    #Argumentos:    1 - Numero de linhas;   2 - Numero de colunas;   3 - N° / qual gráfico estamos plotando agora
    #plt.title("FITNESS MÉDIO POR GERAÇÃO")
    #plt.plot(listaFitnessAux, listaFitness)
    #plt.xlabel("Gerações")
    #plt.ylabel("Fitness Médio")
    #plt.grid()     #Adiciona um quadriculado atrás do gráfico
    
    #ax4 = fig.add_subplot(2, 1, 1)              #grafico 
    ##fitnesses médios
    #ax4.set_title("FITNESS MÉDIO POR GERAÇÃO")
    #ax4.plot(listaFitnessAux, listaFitness)
    #ax4.set_xlabel("Gerações")
    #ax4.set_ylabel("Fitness Médio")
    
    ax3 = fig.add_subplot(gs[1, :-1])
    ax3.set_title("FITNESS MÉDIO POR GERAÇÃO")
    ax3.plot(listaFitnessAux, listaFitness)
    ax3.set_xlabel("Gerações")
    ax3.set_ylabel("Fitness Médio")
    
    #1 - 3D     2 - Pizza       3 - Texto
    #4 - Evo    5 - Evo         6 - Texto

        
    geneX = ""
    geneY = ""
    
    x   = []
    y   = []
    z   = []
    pizza    = []
    colorMap = []
    mostraPizza = False
    if len(populacao) < 20: mostraPizza = True
    
    for i in range(len(populacao)):
        geneX, geneY = separaXY(populacao[i][0])
        x.append(binario_para_float(geneX))
        y.append(binario_para_float(geneY))
        z.append(populacao[i][1])
        
        if mostraPizza == True:
            piz = int((populacao[i][2]*100)/2)
            if piz == 0 : piz = 1
            pizza.append(piz)        #pizza.append(populacao[i][2])
        #Não podemos colocar muitos elementos no gráfico de pizza, se não acontece divisão por 0
        
        
        
        cor = int(((populacao[i][1] + 67.5637) / (67.5637 + 67.5637)) * (100 - 0) + 0)
        colorMap.append(cor)
        #Dados de cor vão de uma escala de 0 a 100, baseados no fitness
        #Como o fitness vai de -67.56 até 67.65, devemos normalizar estes dados.
                                                    #FUNCIONA!

    for i in range(len(listaElites)):
        geneX, geneY = separaXY(listaElites[i][0])
        x.append(binario_para_float(geneX))
        y.append(binario_para_float(geneY))
        z.append(listaElites[i][1])
        
        if mostraPizza == True:
            piz = int((listaElites[i][2]*100)/2)
            if piz == 0 : piz = 1
            pizza.append(piz)        #pizza.append(listaElites[i][2])
        #Não podemos colocar muitos elementos no gráfico de pizza, se não acontece divisão por 0
        
        
        
        cor = int(((populacao[i][1] + 67.5637) / (67.5637 + 67.5637)) * (100 - 0) + 0)
        colorMap.append(cor)
        #Dados de cor vão de uma escala de 0 a 100, baseados no fitness
        #Como o fitness vai de -67.56 até 67.65, devemos normalizar estes dados.
                                                    #FUNCIONA!

    
    #mostramos, o gráfico 3d com a população em tempo real
    ax1 = fig.add_subplot(gs[0, :1], projection = '3d')
    ax1.set_title("POPULAÇÃO EM TEMPO REAL")
    ax1.scatter(x, y, z, c = colorMap, cmap = "cet_linear_kry_0_97_c73")


    #mostramos, ou não, o gráfico da roleta
    if mostraPizza == True:
        ax2 = fig.add_subplot(gs[0, :-1])
        ax2.set_title("Roleta")
        ax2.pie(pizza)
    else:
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.set_title("Roleta")
        ax2.axis("off") #tira as bordas feias do grafico
        ax2.text(0.5, 0.5, "População grande\ndemais para\n mostrar a roleta!", fontsize=12, ha='center', va='center', transform=ax2.transAxes)
        
    randName = ""
    quantNomes = 36
    #Aqui geramos um texto para printar as infos da população:
    textoPopulacao = "Nome:      Gene:              Fitness:\n\n"
    if len(populacao) < 36 : quantNomes = len(populacao)
    for i in range(quantNomes):
        while len(randName) != 6: randName = names.get_first_name()
        textoPopulacao += randName
        textoPopulacao += "     "
        textoPopulacao += populacao[i][0]
        textoPopulacao += "   "
        fitness = populacao[i][1]
        fitness -= 67.56375122070312
        strFitness = str(fitness)
        textoPopulacao += strFitness[:7]
        textoPopulacao += "\n"
        randName = ""
    
    #Aqui mostramos a população Atual
    ax4 = fig.add_subplot(gs[0:, 2])
    ax4.axis("off")
    ax4.set_title("População Atual")
    ax4.text(0.5, 0.5, textoPopulacao, fontsize=10, ha='center', va='center_baseline', fontfamily = "monospace")

    #print(x)
    #print(y)
    #print(z)
    #print("float to int X1: ", float_para_binario(x[0]))
    #print("float to int Y1: ", float_para_binario(y[0]))
    #print("float to int X4: ", float_para_binario(x[3]))
    #print("float to int Y4: ", float_para_binario(y[3]))
    #x = input("xccc")
    plt.draw()
    plt.pause(0.011)
    
    
    
    



def cruzamento(listaGenes):                                 #Recebe a população com seus pesos, e cruza eles de 2 em 2.
    
    nCruzamentos = int(len(listaGenes) // 2) #Quantos pares de cruzamento serão selecionados
                                        #// divide e arredonda para baixo
                                                                      
    for i in range(nCruzamentos):
        somaPesos = sum([gene[2] for gene in listaGenes]) #soma dos pesos dos genes
        
        if(somaPesos == 0):
            somaPesos = 0.0001

        #Aqui escolhemos dois genes com base em seus pesos, usando random.choices
        while(True):
            selecionados = random.choices(listaGenes, weights=[gene[2]/somaPesos for gene in listaGenes], k = 2)
            if(selecionados[0][0] != selecionados[1][0]):
                break                   #Muito ineficiente, mas garante que os dois elementos selecionados sejam diferentes
        
        #print("Selecionamos 0- ", selecionados[0][0], " e 1- ", selecionados[1][0])
        
        
        for i in range(len(listaGenes)):
            if(listaGenes[i][0] == selecionados[0][0]) :
                #print("Individuo = ", listaGenes[i])
                listaGenes[i][2] = 0
                index1 = i
                #print("Individuo dps = ", listaGenes[i])
            if(listaGenes[i][0] == selecionados[1][0]) :
                #print("Individuo = ", listaGenes[i])
                listaGenes[i][2] = 0
                index2 = i
                #print("Individuo dps = ", listaGenes[i])
                
        #Feito isso, vamos cruzar listaGenes[index1] com listaGenes[index2]: (Cruzamento de 2 pontos aleatórios)
        #Primeiro, vamos gerar esses 2 pontos aleatórios:
        corte1 = random.randrange(1, 15)
        corte2 = corte1
        while(corte1 == corte2):                
            corte2 = random.randrange(1, 15)
        
        #print("Corte1 = ", corte1, "  corte2 = ", corte2)
        
        if(corte1 > corte2):    #Garantimos que o primeiro corte aconteça antes do segundo
            aux = corte1
            corte1 = corte2
            corte2 = aux
            
        #print("Corte1 = ", corte1, "  corte2 = ", corte2)
            
        parte1x = listaGenes[index1][0][0:corte1]       #separa os primeiros caracteres 
        parte2x = listaGenes[index1][0][corte1:corte2]  # os proximos 
        parte3x = listaGenes[index1][0][corte2:]        #e os ultimos a partir do indice corte2
        #print('parte1x:',parte1x)
        #print('parte2x:',parte2x)       #prints de teste, se quiser pode remover
        #print('parte3x:',parte3x)
        
        parte1y = listaGenes[index2][0][0:corte1]       #.. 
        parte2y = listaGenes[index2][0][corte1:corte2]  #..
        parte3y = listaGenes[index2][0][corte2:]        #..
        #print('parte1y:',parte1y)
        #print('parte2y:',parte2y)
        #print('parte3y:',parte3y)
        
        #print("Pre corte. index1 = ", listaGenes[index1][0], " index2 = ", listaGenes[index2][0])
        
        listaGenes[index1][0] = parte1x + parte2y + parte3x # forma as duas strings e guarda na lista
        listaGenes[index2][0] = parte1y + parte2x + parte3y
        
        #print("Pos corte. index1 = ", listaGenes[index1][0], " index2 = ", listaGenes[index2][0])
        
        #É isso?

 

def roleta(listaGenes):                                     #Soma 80.06 aos fitnesses da população, e calcula seus pesos (%)
    somaFitness = 0
    
    for i in listaGenes:                #iteramos por todos os fitness de toda a população, e somamos tudo
        i[1] += 80.06377201532881      #Somamos ao minimo possivel
        somaFitness += i[1]         #NOTA: "i" vai receber cada linha da matriz. Só nos interessa a segunda coluna de cada linha.
                                        
    #print("somaFitness é: ", somaFitness)
    
    for i in listaGenes:                #iteramos por todos os genes
        aux = i[1] / somaFitness
        if aux < 0.0001 : aux = 0.0001
        i[2] = (aux)     #probabilidade = (fitness + modulo do valor minimo / soma dos fitness) 
    


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
                    
        geracao1.append([numero, 0, 0]) #colocamos nosso gene no final da lista
    
    fitness_populacao(listaGenes) #Calcula os fitnesses e corrige os limites da função
                    #Seria mais eficiente calcular o fitness enquanto a lista é populada, mas daí teria que arrumar um jeito de corrigir os limites da função



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
        populacao[i][1] = fitness(populacao[i][0])              #Calculamos o novo fitness
        populacao[i][2] = 0                                     #E resetamos sua chance de ser cruzado



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


    
def separaXY(gene):
    tamanho = int(len(gene)/2)
    x = gene[:tamanho]
    y = gene[tamanho:]

    return x, y


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

if(debug == "2" or debug == "Não" or debug == "não" or debug == "Nao" or debug == "nao"):
    tamPopulacao = int(input("Insira o tamanho da população inicial (int): "))          #Pegamos o dado e convertemos em int
    tamGene      = int(input("Insira o tamanho dos genes (int) (recomendado - 16): "))  #(8 bits para X + 8 bits para Y)
    geracoes     = int(input("Insira o número máximo de gerações (int): "))
    eliteReps    = int(input("Insira o número máximo de repetições que um elite pode sofrer (convergência prematura - critério de parada) (int): "))    #Variável usada para identificar uma convergência prematura
    taxaMutacao  = float(input("Insira a taxa de mutação (entre 0.01 e 0.05): "))       #Interpretado como relação (porcentagem/100)
    taxaElitismo = float(input("Insira a porcentagem de elitismo (recomendado - 0.5): "))      #Interpretado como porcentagem (%)
else:
    tamPopulacao = 50
    tamGene      = 16
    geracoes     = 100
    taxaMutacao  = 0.05
    taxaElitismo = 0.5
    eliteReps    = 25

eliteCounter  = 0     
eliteAnterior = ""  #Variáveis usadas para identificar uma convergência prematura

taxaElitismo = taxaElitismo / 100                           #Transformamos a porcentagem no seu equivalente numérico
taxaElitismo = int(math.ceil(taxaElitismo * tamPopulacao))  #Obtemos o valor absoluto de elites por geração

listaGenes   = []    #Matriz. Col 0 - Gene | Col 1 - Fitness | Col 2 - % roleta
listaElites  = []    #Matriz que armazena temporariamente genes removidos da listaGenes na função elitismo()
listaFitness = []
geracoesPassadas = 0


inicializa_genes(tamPopulacao, tamGene, listaGenes) #incializamos a função com os parâmetros acima
print("Sua pop inicial em binario é:")
print_lista(listaGenes)



# Cria a figura e os eixos/matriz
#fig = plt.figure()
#gridspan = fig.add_gridspec(2, 3)

fig = plt.figure(constrained_layout=True)
gs = GridSpec(2, 3, figure=fig)


ax1 = fig.add_subplot(gs[0, :1], projection='3d')   #Ocupa primeiro 1/3 da primeira linha
ax2 = fig.add_subplot(gs[0, 1])   #Ocupa segundo 1/3 da primeira linha
ax3 = fig.add_subplot(gs[1, :-1])   #Vai de 0 até 2/3 da tela, na segunda linha
ax4 = fig.add_subplot(gs[0, :-1])   #Texto, ocupa a direita




#fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(12, 8))


#1 - 3D     2 - Pizza       3 - Texto
#4 - Evo    5 - Evo         6 - Texto

for i in range(geracoes + 1):
    geracoesPassadas += 1
    
    
    #Cálculo do fitness médio aqui
    #Fitness médio da geração, para mostrar ele evoluindo no gráfico
    fitnessMedio(listaGenes, listaFitness)
    #-----------------
    
    

    
    
    #fitness_populacao(listaGenes)  #Acho que essa função nem vai ser necessária,
                                    #já que o fitness sempre é recalculado logo quando um gene é alterado
    #print("--------------------------------------------")
    print(" Nova iteração! Aqui está a lista de genes: ")
    print("")
    print_lista(listaGenes)
    print(" E aqui está a lista de fitness médio: ")
    print("")
    print_lista(listaFitness)
    
    #print("--------------------------------------------")
    
    
    #Critério de parada aqui 
    #checagem de convergência prematura
    if(i == (geracoes) or eliteCounter >= eliteReps): #Se alcançar o número máximo de iterações, ou outro criterio de parada lá
        i = geracoes + 8
        print("LOOP TERMINADO!!! O motivo é...")
        if(eliteCounter >= eliteReps):
            print("Convergência prematura!")
        else:
            print("Limite de gerações excedido!")
        break    #Termina o loop
    #-----------------


    #Elitismo aqui
    print("--------ELITISMO--------")
    elitismo(listaGenes, listaElites, taxaElitismo)         #Obtemos os elites, inserimos eles na listaElites
    #print("Temos ", taxaElitismo, " elites. Eles são: ")
    #print_lista(listaElites)
    print("Nosso elite é: ", listaElites[0])
    print("------------------------")
    #-----------------
    
    
    #Seleção aqui
    #print("--------ROLETA--------")
    roleta(listaGenes) #aqui vamos iterar pela lista e conceder a cada elemento uma porcentagem de escolha
    #print_lista(listaGenes)
    #print("----------------------")
    #-----------------
    
    #Mostramos o Gráfico de Fitness Médio na tela:
    criaGraficos(listaFitness, listaGenes, ax1, ax2, ax3, ax4, listaElites)
    
    #cruzamento aqui
    #print("--------CRUZAMENTO--------")
    cruzamento(listaGenes)
    #print("--------------------------")
    #-----------------
    
    print_lista(listaGenes)
    
    #Mutação aqui
    #print("--------MUTAÇÃO--------")
    #print("Agora vamos mutar  a lista")
    mutacao_populacao(listaGenes, taxaMutacao)
    #print_lista(listaGenes)
    #print("-----------------------")
    #-----------------
    
    #Aqui colocamos os elites de volta na listaGenes
    #print("Elite se repetiu ", eliteCounter, " vezes")
    if(eliteAnterior == listaElites[0]):
        eliteCounter += 1
    else:
        eliteCounter = 0
        eliteAnterior = listaElites[0]
        
    for i in range(len(listaElites)):           #iteramos pela listaElites
        listaGenes.append(listaElites.pop(i))   #Removemos os elites, e colocamos eles de volta na população
    #-----------------


print("Execução do algoritmo executada com sucesso.")
print("Se passaram ", geracoesPassadas, " gerações")
elitismo(listaGenes, listaElites, taxaElitismo)
print("Os melhores genes encontrados foram: ")
print(listaElites)


#fitness_populacao(listaGenes)

bitcoin = input("Digite algo para fechar: ") 

#print("Sua pop mutada é:")
#print_lista(listaGenes)