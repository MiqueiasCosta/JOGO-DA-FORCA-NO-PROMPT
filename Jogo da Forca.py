
import os

print('Ola vamos jogar forca.')
palavra_secreta = input('Digite uma palavra secreta: ')
os.system('cls')
print('Agora passe para quem vai adivinhar a palavra.')
tentativas = 1
while tentativas < len(palavra_secreta):
    letra_de_chute = input('Digite a letra que deseja mas apenas uma: ')
    letras_acertadas = ''
    letras_erradas = ''
    if len(letra_de_chute) == 1:
        tentativas += 1
        if letra_de_chute in palavra_secreta:
            letras_acertadas += letra_de_chute
            print('letras corretas: ', letras_acertadas)
                               

    elif letra_de_chute not in palavra_secreta:
        tentativas += 1
        letras_erradas += letra_de_chute
        print('letras erradas: ', letras_erradas)

        
    elif len(letra_de_chute) > 1:
        print('Digite apenas uma letra.')  
        
        

chute = input('Agora chute a palavra secreta:')
if chute == palavra_secreta:
    print('Parabéns voçê acertou a palavra secreta.')
            
        
else:
    print('A palavra secreta era', palavra_secreta)
    print('Acabaram suas chances, você perdeu.')
    print('digite apenas uma letra')
        

