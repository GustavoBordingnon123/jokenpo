from random import randint
modo_de_jogo = int(input("Para começar a jogar o jokenpo escolha um modo, 1-para humano x humano, 2-para humano x maquina e 3- para maquina x maquina:"))
jogador_A = 5
jogador_B = 5
pontos_do_jogadorA = 0
pontos_do_jogadorB = 0
numero_aleatorio_maquina_A = 0
pontos_da_maquina_A = 0
numero_aleatorio_maquina_B = 0
pontos_da_maquina_B = 0
quantidade_de_partidas = 0
quantidade_de_empates = 0
contador_de_partidas = 0

while modo_de_jogo >3 or modo_de_jogo <1:
    modo_de_jogo = int(input("por favor escolha um número válido, são válidoss os números: 1- para humano x humano, 2- para humano x maquina  3- para maquina x maquina"))
if modo_de_jogo == 1:
    while jogador_A != 0 and jogador_B != 0 or jogador_B != 0 and jogador_A !=0 :
        jogador_A = int(input("Jogador A, escolha sua jogada, 1- para pedra, 2- para papel e 3- para tesoura ou 0 se quiser terminar a partida"))
        while jogador_A > 3 or jogador_A < 0:
            print("Este número é invalido, por favor escolha uma opção dentre 1 a 3")
            jogador_A = int(input("Jogador A, escolha sua jogada, 1- para pedra, 2- para papel e 3- para tesoura ou 0 se quiser terminar a partida"))
        jogador_B = int(input("Jogador B, escolha sua jogada, 1- para pedra, 2- para papel e 3- para tesoura ou 0 se quiser terminar a partida"))
        while  jogador_B > 3  or jogador_B < 0:
            print("Este número é invalido, por favor escolha uma opção dentre 1 a 3")
            jogador_B = int(input("Jogador B, escolha sua jogada, 1- para pedra, 2- para papel e 3- para tesoura ou 0 se quiser terminar a partida"))
        if jogador_A == 1 and jogador_B == 3  or jogador_A == 2 and jogador_B == 1 or jogador_A == 3 and jogador_B == 2:
            print("O jogador A ganhou")
            pontos_do_jogadorA = pontos_do_jogadorA + 1
            quantidade_de_partidas = quantidade_de_partidas + 1
        elif jogador_A == 1 and jogador_B == 1  or jogador_A == 2 and jogador_B == 2 or jogador_A == 3 and jogador_B == 3:
            print("O jogo terminou em empate")
            quantidade_de_partidas = quantidade_de_partidas + 1
            quantidade_de_empates = quantidade_de_empates + 1
        elif jogador_A == 3 and jogador_B == 1  or jogador_A == 1 and jogador_B == 2 or jogador_A == 2 and jogador_B == 3:
            print("O jogador B ganhou")
            pontos_do_jogadorB = pontos_do_jogadorB + 1
            quantidade_de_partidas = quantidade_de_partidas + 1

    else:
        print("fim de jogo")
        if quantidade_de_partidas == 0:
            print("A porcetagem de vitória do jogador A  é: 0")
            print("A porcetagem de vitória do jogador B  é: 0")
            print("A quantidade de partidas foi: 0 ")
            print("A quantidade de empates foi: 0 ")
        if quantidade_de_partidas > 0:
            estatiscas_do_jogadorA = (pontos_do_jogadorA / quantidade_de_partidas) * 100
            estatiscas_do_jogadorB = (pontos_do_jogadorB / quantidade_de_partidas) * 100
            print("A porcetagem de vitória do jogador A, é: ", estatiscas_do_jogadorA, "%" )
            print("A porcetagem de vitória do jogador B, é: ", estatiscas_do_jogadorB, "%")
            print("A quantidade de partidas foi: ", quantidade_de_partidas)
            print("A quantidade de empates foi: ", quantidade_de_empates)
elif modo_de_jogo == 2:
    pontos_do_jogadorA = 0
    pontos_da_maquina_A = 0
    quantidade_de_partidas = 0
    quantidade_de_empates = 0
    while jogador_A != 0:
        jogador_A = int(input("Jogador A escolha sua jogada, 1- para pedra, 2- para papel e 3- para tesoura ou 0 se quiser terminar a partida"))
        while jogador_A > 3 or jogador_A < 0:
            print("Este número é invalido, por favor escolha uma opção dentre 1 a 3")
            jogador_A = int(input("Jogador A escolha sua jogada, 1- para pedra, 2- para papel e 3- para tesoura ou 0 se quiser terminar a partida"))
        numero_aleatorio_maquina_A = randint (1,3)
        print("a maquina escolheu o número =", numero_aleatorio_maquina_A)
        if jogador_A == 1 and numero_aleatorio_maquina_A == 3  or jogador_A == 2 and numero_aleatorio_maquina_A== 1 or jogador_A == 3 and numero_aleatorio_maquina_A == 2:
            print("O jogador A ganhou")
            pontos_do_jogadorA = pontos_do_jogadorA + 1
            quantidade_de_partidas = quantidade_de_partidas + 1
        elif jogador_A == 1 and numero_aleatorio_maquina_A == 1  or jogador_A == 2 and numero_aleatorio_maquina_A == 2 or jogador_A == 3 and numero_aleatorio_maquina_A == 3:
            print("O jogo terminou em empate")
            quantidade_de_partidas = quantidade_de_partidas + 1
            quantidade_de_empates = quantidade_de_empates + 1
        elif jogador_A == 3 and numero_aleatorio_maquina_A == 1  or jogador_A == 1 and numero_aleatorio_maquina_A == 2 or jogador_A == 2 and numero_aleatorio_maquina_A == 3:
            print("A maquina ganhou")
            pontos_da_maquina_A = pontos_da_maquina_A + 1
            quantidade_de_partidas = quantidade_de_partidas + 1
    else:
        print("fim de jogo")
        if quantidade_de_partidas == 0:
            print("A porcetagem de vitória do jogador A é: 0")
            print("A porcetagem de vitória do Maquina  é: 0")
            print("A quantidade de partidas foi: 0 ")
            print("A quantidade de empates foi: 0 ")
        if quantidade_de_partidas > 0:
            estatiscas_do_jogadorA = (pontos_do_jogadorA / quantidade_de_partidas) * 100
            estatiscas_da_maquina_A = (pontos_da_maquina_A / quantidade_de_partidas) * 100
            print("A porcetagem de vitória do jogador A é: ", estatiscas_do_jogadorA, "%")
            print("A porcetagem de vitória da maquina é: ", estatiscas_da_maquina_A, "%")
            print("A quantidade de partidas foi: ", quantidade_de_partidas)
            print("A quantidade de empates foi ", quantidade_de_empates)
elif modo_de_jogo == 3:
    contador_de_partidas = int(input("digite quantas partidas voçê quer que a maquina jogue :"))
    while contador_de_partidas != 0:
        numero_aleatorio_maquina_A = randint(1, 3)
        numero_aleatorio_maquina_B = randint(1, 3)
        print("maquina A escolheu = ", numero_aleatorio_maquina_A)
        print("maquina B escolheu = ", numero_aleatorio_maquina_B)
        if numero_aleatorio_maquina_A == 1 and numero_aleatorio_maquina_B == 3  or numero_aleatorio_maquina_A == 2 and numero_aleatorio_maquina_B == 1 or numero_aleatorio_maquina_A == 3 and numero_aleatorio_maquina_B == 2:
            pontos_da_maquina_A = pontos_da_maquina_A + 1
            quantidade_de_partidas = quantidade_de_partidas + 1
            contador_de_partidas = contador_de_partidas - 1
            print("A maquina A ganhou")
        elif numero_aleatorio_maquina_A == 1 and numero_aleatorio_maquina_B == 1  or numero_aleatorio_maquina_A == 2 and numero_aleatorio_maquina_B == 2 or numero_aleatorio_maquina_A == 3 and numero_aleatorio_maquina_B == 3:
            quantidade_de_partidas = quantidade_de_partidas + 1
            quantidade_de_empates = quantidade_de_empates + 1
            contador_de_partidas = contador_de_partidas - 1
            print("Deu empate")
        elif numero_aleatorio_maquina_A == 3 and numero_aleatorio_maquina_B == 1 or numero_aleatorio_maquina_A == 1 and numero_aleatorio_maquina_B == 2 or numero_aleatorio_maquina_A == 2 and numero_aleatorio_maquina_B == 3:
            print("A maquina b ganhou")
            pontos_da_maquina_B = pontos_da_maquina_B + 1
            quantidade_de_partidas = quantidade_de_partidas + 1
            contador_de_partidas = contador_de_partidas - 1

    else:
        print ("fim de jogo")
        if quantidade_de_partidas == 0:
            print("A porcetagem de vitória do Maquina A é: 0")
            print("A porcetagem de vitória do Maquina B é: 0")
            print("A quantidade de partidas foi: 0 ")
            print("A quantidade de empates foi: 0 ")
        if quantidade_de_partidas > 0:
            estatisticas_da_maquina_A = (pontos_da_maquina_A / quantidade_de_partidas) * 100
            estatisticas_da_maquina_B = (pontos_da_maquina_B / quantidade_de_partidas) * 100
            print("A porcetagem de vitória da maquina A  é: ", estatisticas_da_maquina_A, "%")
            print("A porcetagem de vitória da maquina B é: ", estatisticas_da_maquina_B,"%")
            print("A quantidade de partidas foi: ", quantidade_de_partidas)
            print("A quantidade de empates foi ", quantidade_de_empates)