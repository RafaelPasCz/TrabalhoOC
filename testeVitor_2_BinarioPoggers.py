#Após anlisar de novo as especificações do trabalho, acredito que os genes devam ser armazenados apenas
#em 0's e 1's... e nós estamos armazenando eles em 0's 1's .'s e ' ''s. 
#Aqui, irei corrigir isso.


#To fazendo uns testes nesse arquivo, testando a compatibilidade entre funções

#1 - Inicialização e mutação
        #UPDATE: Compatíveis
        
#2 - 

import random


def print_lista(lista):                                 #Recebe uma lista e printa ela
    for i in lista: #printamos a lista
        print(i)



def inicializa_genes(tamPopulacao, tamGene, geracao1):  #Recebe a lista por endereço
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
                
        geracao1.append(numero) #colocamos nosso gene no final da lista



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



def mutacao_populacao(populacao, tamPopulacao, taxa):   #Muta toda a população
    for i in range(tamPopulacao):
        populacao[i] = mutacao_gene(populacao[i], taxa)



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



def binario_para_float(partes):                 #Recebe string binaria ponto fixo, retorna valor float
   
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







#float -> bin funciona
#bin -> float


#int main()
print("----- Algoritmo Genético -----")
print("Testando bin to float")
while(True):
    numeroB = input("Insira um bin . : ")
    numeroF = binario_para_float(numeroB)
    print("Seu equivalente float é: ", numeroF)
    numeroB = float_para_binario(numeroF)
    print("E bin de novo fica: ", numeroB)





tamPopulacao = int(input("Insira o tamanho da população inicial (int): "))          #Pegamos o dado e convertemos em int
tamGene      = int(input("Insira o tamanho dos genes (int) (recomendado - 16): "))  #(8 bits para X + 8 bits para Y)
taxaMutacao  = float(input("Insira a taxa de mutação (entre 0.01 e 0.05): "))

listaGenes = [] #definimos a lista aonde será armazenado cada indivíduo da geração (em binário)

inicializa_genes(tamPopulacao, tamGene, listaGenes) #incializamos a função com os parâmetros acima

print("Sua pop inicial em binario é:")
print_lista(listaGenes)

print("Sua pop inicial ")

print("Agora vamos mutar ela")

mutacao_populacao(listaGenes, tamPopulacao, taxaMutacao)

print("Sua pop mutada é:")
print_lista(listaGenes)
