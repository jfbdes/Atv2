def listas():
    listanome= []
    listaproduto=[]
    for i in range(2):
        x= str(input('Diga seu nome:'))
        y= str(input('Diga seu produto, temos: salgado, refrigerante, suco, sorvete, cafe, capuccino, bolo e dadinho:')).lower()
        listanome.append(x)
        listaproduto.append(y)
        print(x)
        print(y)

listas()
    


    
