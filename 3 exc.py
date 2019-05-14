def prod():
    for i in range(2):
        x= str(input('Diga seu nome:'))
        y= str(input('Diga seu produto, temos: salgado 4.00, refrigerante 4.50, suco 5.00, sorvete 6.00, cafe 4.00, capuccino 6.00, bolo 4.50 e dadinho:')).lower()
        if x == 'salgado':
            print(x,y,'4.00')
        if y == 'refrigerante':
            print(x,y, '4.50')
        if y == 'suco':
            print(x,y, '5.00')  
        if y == 'sorvete':
            print(x,y,'6.00')
        if y == 'cafe':
            print(x,y,'4.00')
        if y == 'capuccino':
            print(x,y,'6.00')
        if y == 'bolo':
            print(x,y,'4.50')
        if y == 'dadinho':
            print(x,y,'0.50')
            soma +=y
            print (soma)

    

prod()
    
