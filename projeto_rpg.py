import random

arma = []
d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
espada_longa = [1,2,3,4,5,6,7,8]
adaga = [1,2,3,4]
machado = [1,2,3,4,5,6,7,8,9,10]
fuga = [1,2,3,4,5,6]
vida_goblin = 5
forca = 3
print("1 - Espada longa ")
print("2 - Adaga")
print("3 - Machado")
arma_escolhida = int(input('Escolha sua arma: '))
if arma_escolhida == 1:
    arma.append("Espada Longa")
elif arma_escolhida == 2:
    arma.append('Adaga')
elif arma_escolhida == 3:
    arma.append('Machado')
else: 
    print('Opção inválida!')
print('Arma escolhida!')
print('Equanto você caminhava, um goblin apareceu!')
print('Ele diz: Me passe todos os seus pertences ou eu te mato!')

print("1 - Lutar")
print('2 - Fugir (50% de chance de sair ileso)')
print('3 - Entrega pertences (99% de chance de sair ileso)')
print("Sua ação terá consequêcias...")
escolha = int(input("O quê você deseja fazer? "))
if escolha == 1: 
    print('Você irá enfrentar o goblin com sua arma!')
    print("Para acertá-lo, você precisa tirar pelo menos 10 no d20")
    print('Será se você consegue?')
    print("Você saca sua espada e ataca!")
    print('Força = 3')
    d20_ataque = random.choice(d20) + 3
    print('d20 + força : {}'.format(d20_ataque))
    if d20_ataque > 10:
      print('Você acerta o goblin!')
      if arma_escolhida == 1:
        dano_arma = random.choice(espada_longa) + 3
        if d20_ataque >= 19:
          print("Você critou!")
          critico = dano_arma * 2
        print('Você causa {} de dano no goblin'.format(dano_arma))
      if arma_escolhida == 2:
        dano_arma = random.choice(adaga) + 3
        if d20_ataque >= 18:
         print("Você critou!")
         critico = dano_arma * 2
        print('Você causa {} de dano no goblin'.format(dano_arma))
      if arma_escolhida == 3:
        dano_arma = random.choice(machado) + 3
        if d20_ataque == 20:
         print("Você critou!")
         critico = dano_arma * 3
        print('Você causa {} de dano no goblin'.format(dano_arma))
      if dano_arma >= 5 : 
        print('Você matou o goblin e saiu ileso!')
        print("Fim de jogo")
      elif dano_arma >= 3 and dano_arma < 5 :
        print('Você feriu fortemente o goblin! Ele saiu correndo!')
        print("Fim de jogo!")
      elif dano_arma < 3:
        print('Você apenas feriu o goblin, ele reagiu e te matou!')
        print('Você morreu!')
        print("Fim de jogo!")
    else:
      print("Você erra o ataque!")
      print("O goblin reage e te corta!")
      print('Você morreu') 
      print('Fim de jogo!')
if escolha == 2:
  print('Você decidiu fugir!')
  print('Será roletado um 1d6, caso caia par você conseguirá fugir, caso caia impar ele te pega!')
  sorte = random.choice(fuga)
  print("d6 : {}".format(sorte))
  if sorte % 2 == 0 :
    print('Você fugiu!')
  else : 
    print('Você foi pego!')
    print("O goblin roubou seus pertences e te cortou")
    print('Você morreu!')
if escolha == 3:
  print('Você entregou seus pertences e fugiu!')
  print('Você voltou para sua família são e salvo!')
  print('Fim de jogo!')