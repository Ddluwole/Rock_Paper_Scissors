import random

print("Welcome to Rock, Paper, Scissors.\n \tENJOY!!\n")
choice_list= ['R', 'P', 'S']
played_list=[]
game_on=True

while game_on:
    
    computer_choice= random.choice(choice_list)
    player_choice = input("Choose R, P or S:  ").upper()
    print("Player's Choice: %s"%player_choice)
    print("Computer choice: %s" %computer_choice)

    if player_choice[0] in choice_list:
        played_list.append(player_choice[0])
        played_list.append(computer_choice)
        print(played_list)

        if player_choice == computer_choice:
            print('Player (%s) : CPU (%s)' %(played_list[0], played_list[1]))
            print("IT'S A TIE! ")
            played_list.clear()
            continue

        elif (played_list[0] == 'R' and played_list[1]=='S') or (played_list[0] == 'S' and played_list[1]=='P') or (played_list[0] == 'P' and played_list[1]=='R') :
            print('Player (%s) : CPU (%s)' %(played_list[0], played_list[1]))
            print('Player Wins')
            played_list.clear()
            
            

        elif (played_list[0] == 'S' and  played_list[1]=='R') or (played_list[0]=='P' and played_list[1]=='S') or (played_list[0]=='R' and played_list[1]=='P'):
            print('Player (%s) : CPU (%s)' %(played_list[0], played_list[1]))
            print('Computer Wins')
            played_list.clear()

        break
    else:
        print("Error!!\nInvalid input!!!\nPlease choose R, P or S! ")
        continue