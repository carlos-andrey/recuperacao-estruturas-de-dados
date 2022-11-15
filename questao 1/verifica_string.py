def verifica_string(string):
    #lista para comparação individual de caracteres
    list_entrada = []
    for caracter in string:
        #verifica se cada caracter é  ou não uma abertura de parenteses
        if caracter != '(' and caracter != '[' and caracter != '{':
            #cria uma lista com os caracteres em ordem invertida
            ultimo = list_entrada[-1]
            #compara o caracter da entrada com o caracter da entrada invertida      
            if (caracter == ")" and ultimo == "(") or (caracter == "]" and 
            ultimo == "[") or (caracter == "}" and ultimo == "{"): 
                #em caso positivo, remove o ultimo item da lista com os caracteres da entrada
                list_entrada.pop()
            else:
                #em caso negativo, a string é considerada invalida 
                return print(False)
        #caso o caracter seja uma abertura de parenteses, ele é adicionado a lista com os caracteres de entrada
        else: list_entrada.append(caracter)
        #se todos os caracteres em ambas as listas correspondem, a primeira lista é zerada
    if len(list_entrada) == 0:
        #se a lista ficar vazia, é retornado True
        return print(True)
    else:
        #caso a lista não termine vazia, é Retornado um false
        return print(False)
