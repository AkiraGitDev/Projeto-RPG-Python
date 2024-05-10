import random

forca = {}
destreza = {}
constituição = {}
inteligencia = {}
sabedoria = {}
carisma = {}

atributos = [forca, destreza, constituição, inteligencia, sabedoria, carisma]

humano = [1, 1, 1, 1, 1, 1]
anao = [0, -1, 2, 0, 1, 1]
elfo = [0, 1, -1, 2, 0, 0]
goblin = [0, 2, 0, 1, 0, -1]
golem = [2, 0, 1, 0, 0, -1]

racas = {
    humano, 
    anao, 
    elfo,
    goblin,
    golem
}

def escolher_raca():
    


d20 = []
for i in range(1,20):
    d20.append(i)
print('Rolando dado...')
rolagem = random.choice(d20)
if rolagem == 20:
    print('CRÍTICO!')
    print('Sua rolagem deu: {}'.format(rolagem))
else:
    print('Sua rolagem deu: {}'.format(rolagem))

pericia_luta = int(5)
acerto = rolagem + pericia_luta
print('Rolagem + Luta = {}'.format(acerto))

espada_longa = []
if rolagem != 20:
    for i in range(1,6):
        espada_longa.append(i)
    rolagem_dano = random.choice(espada_longa)
elif rolagem == 20:
    for i in range(1,6):
        espada_longa.append(i)
    rolagem_dano = random.choice(espada_longa) * 2

definir_defesa = []
for i in range (10,25):
    definir_defesa.append(i)
defesa = random.choice(definir_defesa)
print('A Defesa do seu alvo é: {}'.format(defesa))

if defesa > acerto:
    print('Você errou o ataque...')
else: 
    dano = rolagem_dano + forca
    print('Você acertou o ataque!')
    print('Sua rolagem de dano deu: {}'.format(dano))