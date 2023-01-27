import functions as f

print("CLI_Text_Tools!")
def ajuda():
    print("""Comandos:
    sair - Sair do programa | voltar - Sair do comando |
    espelho - Inverter frases | iniciais - Iniciais maiúsculas |
    camel - Alterna maiúsculas e minúsculas | rot13 - Cifra de César |
    maius - Texto todo maiúsculo | minus - Texto todo minúsculo""")
#print("sair - Sair do programa")
#print("voltar - Sair do comando")
#print("espelho - Inverter frases")
#print("iniciais - Iniciais maiúsculas")
#print("camel - Alterna maiúsculas e minúsculas")
#print("rot13 - Cifra de César")
#print("maius - Texto todo maiúsculo")
#print("minus - Texto todo minúsculo")

ajuda()

while True:
    comando = input("> ").lower()
    if comando == "sair":
        break

    # AJUDA
    elif comando == "ajuda":
        ajuda()
    # ESPELHO
    elif comando == "espelho":
        while True:
            esp = input("esp- ")
            if esp.lower() == "voltar":
                break
            else:
                print("->",f.inverte_frase(esp))

    # INICIAIS
    elif comando == "iniciais":
        while True:
            ini = input("ini- ")
            if ini.lower() == "voltar":
                break
            else:
                print("->",f.iniciais(ini))

    # CAMELCASE
    elif comando == "camel":
        while True:
            cam = input("cam- ")
            if cam.lower() == "voltar":
                break
            else:
                print("->",f.camelcase(cam))

    # ROT13
    elif comando == "rot13":
        while True:
            rot = input("r13- ")
            if rot.lower() == "voltar":
                break
            else:
                print("->",f.rot13(rot))

    # MAIUS
    elif comando == "maius":
        while True:
            mai = input("mai- ")
            if mai.lower() == "voltar":
                break
            else:
                print("->",mai.upper())

    # MINUS
    elif comando == "minus":
        while True:
            minus = input("min- ")
            if minus.lower() == "voltar":
                break
            else:
                print("->",minus.lower())

    # COMANDO INVÁLIDO
    else:
        print("<<Comando inválido. Digite 'ajuda' para ver os comandos.>>")
