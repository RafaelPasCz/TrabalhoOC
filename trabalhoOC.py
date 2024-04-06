
def float_para_binario(numero):
    casas = 3
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
    
    return resultado_float




def funcao(x,y):
    z = (pow(x,5)) - (10*(pow(x,3))) + (30*x) - (pow(y,2)) + (21*y)
    return z

x = 1.126033
y = 2.5
i = 0
m = 100000
ponto = '.'
bx = float_para_binario(x)
by = float_para_binario(y)
print('bx: ',bx)
print('by: ',by)
a = binario_para_float(bx)
b = binario_para_float(by)
print('a: ',a)
print('b: ',b)


#z = funcao(x,y) 
#print('resultado: ',z)





