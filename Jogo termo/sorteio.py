import random

def get_palavra():
    with open('./palavras.txt', 'r') as file:
        palavras = file.readlines()

    return random.choices(palavras)[0].upper().strip()


palavra_secreta = get_palavra()
