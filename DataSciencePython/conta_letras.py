def contar_ocorrencia_letras_frases(lista):
    dicio = {}
    for palavra in lista:
        palavra = palavra.lower()
        if palavra not in dicio.keys():
            dicio[palavra] = 1
        else:
            valor = dicio[palavra] + 1
            dicio[palavra] = valor
        
        resultado = [f'"{x}" = {y}' for x,y in dicio.items()]
    return resultado


def contar_letras(texto):
    contador = 0
    for _ in texto:
        contador += 1
    return contador


if __name__ =='__main__':
    texto = 'Um forte indicador de que já há avanços de Democratização de Dados nas organizações é observar quantas pessoas tem acesso a Dados.'
    print(contar_ocorrencia_letras_frases(texto))
    print(contar_letras(texto))