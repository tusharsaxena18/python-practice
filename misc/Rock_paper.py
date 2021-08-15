import random

list=['Rock','Paper','Scissors']
player = False

while player == False:
    comp=list[random.randint(0,2)]
    player=input("Rock,Paper or Scissors?: ")
    
    if player == comp:
        print("Tie")
    
    elif player == "Rock":
        if comp =="Paper":
            print("You Lose "+comp +" covers "+player)
        else:
            print("You win! ", player, "smashes ",comp)
    
    elif player =="Paper":
        if comp =="Scissors":
            print("You lose! ",comp, "cut ",player)
        else:
            print("You win! ",player, "covers ",comp)
    
    elif player == "Scissors":
        if comp == "Rock":
            print("You lose... ",comp, "smashes ",player)
        else:
            print("You win!",player, "cut",comp)
    
    else:
        print("Invalid Choice")
    
    comp=list[random.randint(0,2)]
    
    print("Do you want to play again")
    end = input()
    if end  in ['y']:
        player=False
    else:
        player=True
        print("Press any key to exit: ")
        end=input("")
        if end in ['F']:
            exit()
        else:
            exit()
    