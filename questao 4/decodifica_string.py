def decodificaString(entrada):
    num = 0 #variavel para fazer a multiplicação
    string = '' #variavel para compor a multiplicação
    stack = [] #variavel para armazenar as letras a serem multiplicadas

    for caracter in entrada:
        # verifica se o caracter é um numero
        if caracter.isdigit():
            num = num*10 + int(caracter)
        # verifica se o caracter é um '['
        elif caracter == "[":
            stack.append(string)
            stack.append(num)
            string = ''
            num = 0
        # verifica se o caracter é um letra
        elif caracter.isalpha():
            if caracter.isdigit() is False:
                string += caracter
        # verifica se o caracter é um ']'
        elif caracter == ']':
            pre_num = stack.pop()
            pre_string = stack.pop()
            string = pre_string + pre_num * string
    return string
