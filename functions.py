# Funções para rodar no CLI_Text_Tools

def inverte_frase(frase):
    frase = list(frase)
    esarf = []
    count = len(frase) -1
    while count > -1:
        esarf.append(frase[count])
        count -= 1

    return "".join(esarf)
        
def iniciais(frase):
    frase = frase.split(" ")
    nova_frase = []
    for palavra in frase:
        palavra = palavra[0].upper() + palavra[1:]
        nova_frase.append(palavra)
    return nova_frase[0] + " " + " ".join(nova_frase[1:])

def camelcase(frase):
    nova_frase = ""
    for indice in range(len(frase)):
        if indice % 2 == 0:
            nova_frase += frase[indice].upper()
        else:
            nova_frase += frase[indice].lower()
    return nova_frase

def da_volta(inicio, fim, rot):
    resultado = rot

    while(resultado > fim):
        excesso = resultado - fim
        resultado = inicio + (excesso - 1)

    return resultado

def rot13(frase):
    rot = 13
    nova_frase = ""

    for caractere in frase:
        valor = 0
        ch = ord(caractere)
        if (ch >= 65 and ch <= 90):
            rot13 = ch + rot
            valor = da_volta(65, 90, rot13)
        elif (ch >= 97 and ch <= 122):
            rot13 = ch + rot
            valor = da_volta(97, 122, rot13)
        else:
            valor = ch

        nova_frase += chr(valor)

    return nova_frase
