#Esse arquivo testa e obtém os valores de X e Y equivalentes ao máximo e mínimo da função
#Coincidentemente, os dois valores são inversos

#VALOR MÁXIMO DE X = 1.1260325
#VALOR MÁXIMO DE Y = 2.5
##VALOR MÁXIMO DE Z = 67.56375122070312

#VALOR MÍNIMO DE X = -1.12603
#VALOR MÍNIMO DE Y = -2.5
##VALOR MÍNIMO DE Z = -67.56375122070312



def ZfuncaoXY(x,y):###############################################################################################################
    z = (pow(x,5)) - (10*(pow(x,3))) + (30*x) - (pow(y,2)) + (21*y)
    return z


def ZfuncaoX(x):    #Aqui, Y == 2.5
    y = 2.5
    z = (pow(x,5)) - (10*(pow(x,3))) + (30*x) - (pow(y,2)) + (21*y)
    return z

def ZfuncaoY(y):    #Aqui, Y == 2.5
    x = 1.1260325 #Valor ideal de X
    z = (pow(x,5)) - (10*(pow(x,3))) + (30*x) - (pow(y,2)) + (21*y)
    return z


#while(True):
#    print("Coiso ", ZfuncaoXY(1.1260325, 2.5))




minimoX = -1.12603
minimoY = -2.5
minimoZ = ZfuncaoXY(minimoX, minimoY)

print("O menor valor possível para a função é... ... ... ", minimoZ)

print("Maior:")

maximoX = -2.5
maximoZ = minimoZ

#for i in range(50):   #{-2.5 <= X <= 2.5}
#    maximoX += 0.1
#    nZ = ZfuncaoX(maximoX)
#    print("NZ EH ", nZ)
#    if(nZ > maximoZ):
#        maximoX = nZ
        


#for x in range(112403250, 112503250):  # Ampliando a busca para um grid mais fino
#    x /= 100000090  # Convertendo para float
#    nZ = ZfuncaoX(x)
#    print("NZ EH ", nZ)
#    if nZ > maximoZ:
#        maximoX = x
#        maximoZ = nZ

#print("Maximo Z encontrado: ", maximoZ)
#print("Para o X = ", maximoX)
    


#Abaixo buscamos o valor ideal de Y

maximoY = 2.0

for y in range(2400000, 2510000):  # Ampliando a busca para um grid mais fino
    y /= 1000000  # Convertendo para float
    nZ = ZfuncaoY(y)
    print("NZ EH ", nZ)
    if nZ > maximoZ:
        maximoY = y
        maximoZ = nZ

print("Maximo Z encontrado: ", maximoZ)
print("Para o Y = ", maximoY)