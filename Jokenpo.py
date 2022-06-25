from random import randint

'''in this variavel, the first item in the list is the (A) points, the second is the (B) points, the third is to the how many draws 
the game had, and the final item is to the how many games had'''
statiscs_of_the_game = [0,0,0,0] 
player_A_or_computerA_move = 0
player_B_or_computerB_move = 0

def game_mode():
    print()
    print("Sumarry of game modes:")
    print("1- player vs player")
    print("2- player vs computer")
    print("3- computer vs computer")
    print("4- exit")
    print()
    chosen_game_mode = int(input("please, choose one mode to play now: "))
    while chosen_game_mode < 1 or chosen_game_mode > 4:
        chosen_game_mode = int(input("this option is invalid, please chosse one mode of the summary: "))
    return chosen_game_mode

def statistics(player_A_or_computerA_move,player_B_or_computerB_move):
    if player_A_or_computerA_move == 2 and player_B_or_computerB_move == 1 or player_A_or_computerA_move == 3 \
    and player_B_or_computerB_move == 2 or player_A_or_computerA_move == 1 and player_B_or_computerB_move == 3:
        print("the (A) wins ")
        print()
        statiscs_of_the_game[0] += 1
        statiscs_of_the_game[3] += 1
    
    elif player_B_or_computerB_move == 2 and player_A_or_computerA_move == 1 or player_B_or_computerB_move == 3 \
    and player_A_or_computerA_move == 2 or player_B_or_computerB_move == 1 and player_A_or_computerA_move == 3:
        print("the (B) wins ")
        print()
        statiscs_of_the_game[1] += 1
        statiscs_of_the_game[3] += 1

    elif player_A_or_computerA_move == player_B_or_computerB_move:
        print("the match endeed in a draw ")
        print()
        statiscs_of_the_game[3] += 1

    return statiscs_of_the_game

def final_statistics_print(statiscs_of_the_game):
    print()
    print("the (A) percentage of wins is = ", (statiscs_of_the_game[0]/statiscs_of_the_game[3]) * 100,"%")
    print("the (B) percentage of wins is = ", (statiscs_of_the_game[1]/statiscs_of_the_game[3]) * 100,"%")
    print("the total of draws matchs is = ", statiscs_of_the_game[2] )
    #the total of game starts in 1, cause if you ended the game with zero games, the calculator gonna bug by division por zero
    print("the total of matchs is = ",statiscs_of_the_game[3])


game_mode_chossed = game_mode()
print()
print("Sumarry of moves:")
print("1- Rock")
print("2- Paper")
print("3- Scissors  ")
print("4- exit")
print()

while game_mode_chossed != 4:

    while game_mode_chossed == 1:

        player_A_or_computerA_move = int(input("please player A, choose what move you go do now: "))
        while player_A_or_computerA_move < 1 or player_A_or_computerA_move > 4:
            player_A_or_computerA_move = int(input("this option is invalid, please chosse one mode of the summary:  "))

        player_B_or_computerB_move = int(input("now its the player B turn, choose what move you go do now: "))
        while  player_B_or_computerB_move < 1 or  player_B_or_computerB_move > 4:
            player_B_or_computerB_move = int(input("this option is invalid, please chosse one mode of the summary:  "))

        if player_A_or_computerA_move == 4 or player_B_or_computerB_move == 4:

            #the player a gonna be 0, to not bug if you join 2 times or more in the first game mode
            player_A_or_computerA_move = 0

            print("the game is over")
            final_statistics_print(statiscs_of_the_game)

            #we turn back the statiscs to the next time you join in this mode the code starst from zero again
            statiscs_of_the_game = [0,0,0,0] 
            game_mode_chossed = game_mode()

        statiscs_of_the_game = statistics(player_A_or_computerA_move,player_B_or_computerB_move)


    while  game_mode_chossed == 2: 
        player_A_or_computerA_move = int(input("please player A, choose what move you go do now: "))
        while player_A_or_computerA_move < 1 or player_A_or_computerA_move > 4:
            player_A_or_computerA_move = int(input("this option is invalid, please chosse one mode of the summary:  "))

        player_B_or_computerB_move = randint (1,3)
        print("computer B move = ",player_B_or_computerB_move)

        if player_A_or_computerA_move == 4:

            #the player a gonna be 0, to not bug if you join 2 times or more in the first game mode
            player_A_or_computerA_move = 0

            print("the game is over")
            final_statistics_print(statiscs_of_the_game)

            #we turn back the statiscs to the next time you join in this mode the code starst from zero again
            statiscs_of_the_game = [0,0,0,0] 
            game_mode_chossed = game_mode()

        statiscs_of_the_game = statistics(player_A_or_computerA_move,player_B_or_computerB_move)

    while game_mode_chossed == 3: 
        matches = int(input("please, digit how many matches you wanna to the computers play: "))
        for timer in range(matches):
            player_A_or_computerA_move = randint (1,3)
            print("computer A move = ",player_B_or_computerB_move)
            player_B_or_computerB_move = randint (1,3)
            print("computer B move = ",player_B_or_computerB_move)
        
            statiscs_of_the_game = statistics(player_A_or_computerA_move,player_B_or_computerB_move)
        
        print("the game is over")
        final_statistics_print(statiscs_of_the_game)
        #we turn back the statiscs to the next time you join in this mode the code starst from zero again
        statiscs_of_the_game = [0,0,0,0] 
        game_mode_chossed = game_mode()

print("end of the code")
