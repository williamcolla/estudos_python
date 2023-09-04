palavra_secreta = 'cabelo'
letra_acertada = ''
tentativas = 0


while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    nova_palavra = ''
    for letra_nova in palavra_secreta:
        if letra_nova in letra_acertada:
            nova_palavra += letra_nova
        else:
            nova_palavra += '*'
    
    print(f'Palavra formada: {nova_palavra}')
    
    if nova_palavra == palavra_secreta:
        print('Parabéns, você acertou a palavra secreta!')
        print(f'A palavra era {palavra_secreta}.')
        print(f'Tentativas: {tentativas}')
        break
        #letra_acertada = ''
        #tentativas = 0