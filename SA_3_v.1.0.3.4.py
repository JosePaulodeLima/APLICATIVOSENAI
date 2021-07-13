def linha ():
    print ()
    print ('_' *42)
    print ()
    
print('=' * 10,'CALCULADORA DE TROCO','=' * 10)
print ()
valorDaCompra = float(input('Digite o valor da sua compra: '))
linha ()
valorRecebido = float(input('Agora digite o valor o recebido pela compra: '))
linha ()
valorTroco = valorRecebido - valorDaCompra
print ('Seu troco é de: R$ %.2f' % valorTroco)
cedulas = 200
moedas = 1
totalCedulas = 0
valorRestante = valorTroco
moeda = 'celula (s)'

while True:
    if cedulas  <= valorRestante:
        totalCedulas +=1
        valorRestante -= cedulas
        
    else:
        
        if totalCedulas > 0:
            print (f'O seu troco possui {totalCedulas} {moeda} de: R$ %.2f' % cedulas)
        if cedulas == 200:
            cedulas = 100
        elif cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
            cedulas = 1
        elif cedulas == 1:
            moeda = 'moeda (s)'
            cedulas = 0.5
        elif cedulas == 0.5:
            moeda = 'moeda (s)'
            cedulas = 0.25
        elif cedulas == 0.25:
            moeda = 'moeda (s)'
            cedulas = 0.10
        elif cedulas == 0.10:
            moeda = 'moeda (s)'
            cedulas = 0.05
        elif cedulas == 0.05:
            moeda = 'moeda (s)'
            cedulas = 0.01    
        totalCedulas = 0
        if valorTroco == 0:
            break
       

    
                
