import random

d20 = []
for i in range(1,20):
    d20.append(i)
print('Rolando dado...')
rolagem = random.choice(d20)
print('Sua rolagem deu: {}'.format(rolagem))

atributo_forca = 3
atributo_destreza = {}
atributo_constituição = {}
atributo_inteligencia = {}
atributo_sabedoria = {}
atributo_carisma = {}

atributos = [atributo_forca, atributo_destreza, atributo_constituição, atributo_inteligencia, atributo_sabedoria, atributo_carisma]

pericia_luta = int(5)
acerto = rolagem + pericia_luta
print('Rolagem + Luta = {}'.format(acerto))

espada_longa = []
for i in range(1,6):
    espada_longa.append(i)
rolagem_dano = random.choice(espada_longa)

definir_defesa = []
for i in range (10,25):
    definir_defesa.append(i)
defesa = random.choice(definir_defesa)
print('A Defesa do seu alvo é: {}'.format(defesa))

if defesa > acerto:
    print('Você errou o ataque...')
else: 
    dano = rolagem_dano + atributo_forca
    print('Você acertou o ataque!')
    print('Sua rolagem de dano deu: {}'.format(dano))