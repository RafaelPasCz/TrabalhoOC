def separaXY(gene):
    tamanho = int(len(gene)/2)
    x = gene[:tamanho]
    y = gene[tamanho:]
    print("x - ", x, " - y - ", y)
    
    
gene = "0011011010001101"
separaXY(gene)