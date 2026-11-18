import random
players_score=0
computers_score=0
options=("rock" ,"scissors" ,"paper")
play_again="yes"
while play_again== "yes":
    players_choice=input("choose rock , paper or scissors: ")
    computers_choice=random.choice(options)
    print("i chose " + computers_choice)
    if computers_choice=="paper" and players_choice == "scissors":
            print("you win ")
            players_score += 1
            print(computers_score)
            print(players_score)
            play_again=input("play again? yes or no ")
    elif players_choice=="paper" and computers_choice == "scissors":
            print("i win")
            computers_score+=1
            print(computers_score)
            print(players_score)
            play_again=input("play again? yes or no ")
    elif players_choice=="rock" and computers_choice == "scissors":
            print("you win")
            players_score+=1
            print(computers_score)
            print(players_score)
            play_again=input("play again? yes or no ")
    elif players_choice=="scissors" and computers_choice == "rock":
            print("i win")
            computers_score+=1
            print(computers_score)
            print(players_score)
            play_again=input("play again? yes or no ")
    elif players_choice == "paper" and computers_choice == "rock":
        print("you win")
        players_score += 1
        print(computers_score)
        print(players_score)
        play_again=input("play again? yes or no ")
    elif players_choice == "rock" and computers_choice == "paper":
        print("i win")
        computers_score += 1
        print(computers_score)
        print(players_score)
        play_again=input("play again? yes or no ")
    elif computers_choice==players_choice:
        print("its a draw")
        print(computers_score)
        print(players_score)
        play_again=input("play again? yes or no ")
print("the final score is...")
print(computers_score)
print(players_score)
