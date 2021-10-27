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
