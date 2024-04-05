from binary_fractions import Binary
def funcao(x,y):
    z = (pow(x,5)) - (10*(pow(x,3))) + (30*x) - (pow(y,2)) + (21*y)
    return z

def truncar(string, ponto):
    prefixo = "0b" #prefixo porque se não tiver esse indicador a fução de transformar char em string binária não vai funcionar
    for indice, char in enumerate(string):
        if char == ponto:
            indice = indice + 4  
            string = string[:indice]
            string = prefixo + string
            return string

x = 1.126033
y = 2.5
i = 0
m = 100000
ponto = '.'
#for i in range(m):
bx = Binary(x).rfill(3)._string #transforma x em string de chars representando o binário de x
by = Binary(y).rfill(3)._string #transforma y em string de chars representando o binário de y
bx = truncar(bx,ponto) #trunca a string para 3 casas após a vírgula
by = truncar(by,ponto) # ...
print("bx: ",bx)
print("by: ",by)
bx = Binary(bx).rfill(3) #transforma string de chars em string binária
by = Binary(by).rfill(3) #...
print("bx: ",bx)
print("by: ",by)
b = bx + by
print(b)
print("fim")
#z = funcao(x,y) 
#print('resultado: ',z)


