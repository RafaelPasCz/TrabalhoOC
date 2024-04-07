import random

def elitismo(geracao):
    melhorgene = geracao[0]
    for i in range(len(geracao)):
        if geracao[i] > melhorgene:
            melhorgene = geracao[i]
    return i


def cruzamento(pontobinx,pontobiny): #(pontosaseremcruzados)
    #se a entrada for a string grande de 16 bits, separada por espaço
    #pontosaseremcruzados = pontos.split() separa a string em duas no espaço e guarda as duas metades em uma lista
    #pontocruzadox = pontosaseremcruzados[0]
    #pontocruzadoy = pontosaseremcruzados[1]
    pontoscruzados = [None] * 2 #lista para guardar as 2 strings de retorno
    parte1x = pontobinx[:2] #separa os 2 primeiros caracteres 
    parte2x = pontobinx[2:6] # os proximos 4
    parte3x = pontobinx[6:] #e os ultimos a partir do indice 6
    print('parte1x:',parte1x) #prints de teste, se quiser pode remover
    print('parte2x:',parte2x)
    print('parte3x:',parte3x)
    parte1y = pontobiny[:2] #..
    parte2y = pontobiny[2:6] #..
    parte3y = pontobiny[6:] #..
    print('parte1y:',parte1y)
    print('parte2y:',parte2y)
    print('parte3y:',parte3y)
    pontoscruzados[0] = parte1x + parte2y + parte3x # forma as duas strings e guarda na lista
    pontoscruzados[1] = parte1y + parte2x + parte3y #se quiser pode somar as duas strings da lista para criar uma de 16 caracteres e retornar isso
    return pontoscruzados

def calculafit(pontosbinx,pontosbiny,t):
    pontosdecx = [None] * t
    pontosdecy = [None] * t
    pontosdecz = [None] * t #cria listas para guardar os valores em decimal 
    for i in range (t):
        pontosdecx[i] = binario_para_float(pontosbinx[i]) #converte de binario para float r guarda num vetor
        pontosdecy[i] = binario_para_float(pontosbiny[i]) #..
        pontosdecz[i] = funcao(pontosdecx[i],pontosdecy[i]) #calcula o fitness da geração
    return pontosdecz #retorna a lista com todos os fitness associados a cada índice de par (x,y)
    


def roleta(ger): #ger = lista contendo os fitness da geração, cada índice corresponde a um par (x,y) da geração
    t = len(ger)
    p=[None]*t  #declara lista das porcentagens
    soma = sum(ger) #soma todos os fitness da geração
    for i in range (t):
        p[i] = (ger[i] + 75.15625 / soma) * 100 #probabilidade = (fitness + modulo do valor minimo / soma dos fitness) * 100 

    escolhas=random.choices(population=ger,weights=p,k=t)   #metodo random.choices retorna lista com t posições-
                                                            #-todos os indices são ocupados com um sorteio de um membro de ger-
                                                            #-todos baseados em o peso passado em p respectivamente, as probabilidades não-
                                                            #-são cumulativas, então todos os sorteios são igualmente válidos, escolhi o primeiro da-
                                                            #-lista para ser o gene sorteado
    sorteado = escolhas[0]
    for i in range(t):
        if sorteado == ger[i]:
            return ger[i] #achar o índice de ger que foi sorteado e retornar


    
def float_para_binario(numero):
    if numero > 2.5:
        return 2.5
    if numero < -2.5:
        return -2.5
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

    binario_representacao = binario_inteiro + '.' + ''.join(binario_decimal) #soma as strings para juntar o inteiro e decimal
    
    binario_representatacao_sinal = sinal_bit + binario_representacao
    
    return binario_representatacao_sinal





def binario_para_float(string_binaria):
   
    bit_sinal = string_binaria[0]    # Verifica o bit de sinal e seta aflag de positivo ou negativo
    e_negativo = True if bit_sinal == '1' else False
    
    
    partes = string_binaria[1:].split('.') # separa a parte inteira e a parte fracionária da string binária e guarda em vetor partes
    if len(partes) == 1:
        parte_inteira = partes[0] #se so houver parte inteira, parte decimal será 0
        parte_decimal = '0' 
    else:
        parte_inteira = partes[0]
        parte_decimal = partes[1]
    
    if parte_inteira == "100":
        if parte_decimal == "00000": #tratar 0 negativo
            parte_inteira = "000"
   
    parte_inteira_float = int(parte_inteira, 2) #converte a parte inteira binaria pra inteiro decimal
    
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




def funcao(x,y):
    z = (pow(x,5)) - (10*(pow(x,3))) + (30*x) - (pow(y,2)) + (21*y)
    return z

x = -2.5
y = -2.5
i = 0
m = 100000
ponto = '.'
populacao = ['001.10010 101.10010','110.11001 010.10110']
pontosbinx = [None] * len(populacao)
pontosbiny = [None] * len(populacao)
#-------testes das funções de conversão----------
bx = float_para_binario(x)
by = float_para_binario(y)
print('bx: ',bx)
print('by: ',by)
a = binario_para_float(bx)
b = binario_para_float(by)
print('a: ',a)
print('b: ',b)
#-------------------------------------------------
#----------teste da roleta--------------
geracaoteste = [22.5,42.7,98.1,40.8]
escolha = roleta(geracaoteste)
print(escolha)
#-------------------------------------
#---------teste de calculafit--------
geracao = [None] * len(populacao)
for i in range (len(populacao)):
    pontosbinsep = populacao[i].split()
    print('pontosbinsep: ',pontosbinsep)
    pontosbinx[i] = pontosbinsep[0]
    pontosbiny[i] = pontosbinsep[1]
geracao=calculafit(pontosbinx,pontosbiny,len(populacao))
print('geracao: ',geracao)
#------------------------------------
#------teste de cruzamento-------
pontoa = "101.00111"
pontob = "010.10001"
cruzados=cruzamento(pontoa,pontob)
print('cruzados:',cruzados)
#---------------------------------
#-------teste de elitismo-------

