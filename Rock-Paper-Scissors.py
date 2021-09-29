import random
def Rock_Paper_Scissors():
    game_list = ['rock','paper','scissors','stop']
    p1_score = 0
    computer_score =0
    while True:
        p1 = input('rock,paper or scissors? :')
        p2 = random.choice(game_list)
        if p1 not in game_list:
             print('please make your choice correctly')
        elif p1 == p2:
            print('Draw')
        elif p1 == "rock":
            if p2 == "scissors":
                p1_score +=1
                print("Rock smashes scissors! You win!")
            else:
                computer_score +=1
                print("Paper covers rock! You lose.")
        elif p1 == "paper":
            if p2 == "scissors":
                computer_score +=1
                print("Scissors cuts paper! You lose!")
            else:
                p1_score +=1
                print("Paper covers rock! You win!")
        elif p1 == "scissors":
            if p2 == "paper":
                p1_score +=1
                print("Scissors cuts paper! You win!")
            else:
                computer_score +=1
                print("Rock smashes scissors! You lose.")
        else:
            if p1 =='stop':
                play_again = input("Do you want to stop the game? (y/n): ")
                if play_again.lower() == "y":
                    print(f'Player score ={p1_score}, Computer score = {computer_score}')
                    if p1_score == computer_score:
                        print('Draw')
                    elif p1_score > computer_score:
                        print('Player Wins')
                    elif p1_score < computer_score:
                        print('Computer Wins')
                    break
                else:
                    continue
Rock_Paper_Scissors()