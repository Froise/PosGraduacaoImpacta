#exemplo simples de calculadora com classe e função

class calculadora():


    def soma(self,x,y):
        return x + y


    def subtracao(self,x,y):
        return x - y


    def multiplicacao(self,x,y):
        return x * y


    def divisao(self,x,y):
        if y == 0:
            resultado = "Valor não pode ser 0"
        else:
            resultado = x / y
        return resultado


if __name__=='__main__':

    c = calculadora()

    n1 = int(input())
    n2 = int(input())
    
    print('Resultado das contas')
    print(f"{n1} + {n2} = {c.soma(n1,n2)}")
    print(f"{n1} - {n2} = {c.subtracao(n1,n2)}")
    print(f"{n1} * {n2} = {c.multiplicacao(n1,n2)}")
    print(f"{n1} / {n2} = {c.divisao(n1,n2)}")