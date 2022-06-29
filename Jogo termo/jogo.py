print('Bem-vindo ao jogo TERMO!!')
print ("Seu objetivo é tentar acertar a palavra secreta")
print ("Caso você acerte, a letra será colocada na palavra para que você chegue mais perto de acertar")
print ("Caso você erre, você percerá uma chance, você tem no máximo seis tentativas")

from sorteio import palavra_secreta
estado_atual = ['_'] * len(palavra_secreta)

palavras_escolhidas = []
palavras_fora = []
cont = 0
acertou = False

while not acertou:
    palavra = input('\n\nDigite uma palavra:').strip().upper()
    
    if palavra == '':
        print('ERRO!! precisa escrever algo!!')
        continue

    if palavra.isnumeric():
        print('ERRO!! Apenas letras!')
        continue
    
    print()
    cont -=1
    print('=+'*20)
    print(f'Você ainda tem {cont+6} tentativas!! ')
    print('=+'*20)
    print()
    
    for c in palavra:
        index = palavra_secreta.find(c)
        if index !=-1: 
            estado_atual[index] = c
        else:
            palavras_fora.append(c)
    print('Essas letras não tem na palavra:')
    print(palavras_fora)
    palavras_fora.clear()
    
    print()
    print('='*35)
    print(estado_atual, 'Atualizado!')
    print('='*35)

        
       
    while palavra in palavras_escolhidas:
        print('Palavra já foi escolhida!!')
        palavra = input('\n\nDigite uma palavra:').strip().upper()
    palavras_escolhidas.append(palavra)

 
    print ("As letras que você já tentou são:")
    for item in palavras_escolhidas:
        print(item, end=" ")
    print()

    if palavra_secreta == palavra:
        print('-='*20)
        print('PARABÉNS!! Você acertou a palavra secreta!')
        print(f'A palavra era: {palavra_secreta}')
        print('-='*20)
        acertou = True
    

    elif cont < -6:
        print('Acabou as tentativas. Infelizmente você não conseguiu acertar!!')
        print(estado_atual)
        print(f'A palavra era: {palavra_secreta}')
        break

    
   
       
            
            
     

