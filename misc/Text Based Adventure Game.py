first_choice=input("You have reached a crossroad would you like to go to left or right: ")

if first_choice in ['Left','left']:
    second_choice=input("You have encountered a haunted house. Would you like to go in?: ")
    if second_choice in ['yes','Yes']:
        fourth_choice= print("You found a chest.You found Level 1 armor in it. What a luck!")
    elif fourth_choice in ['no','No']:
        fifth_choice=input("That was for better. Its not like you would get some armor inside a chest: ")
    else:
        print("Invaild Choice")
    print("So we got rid of the house")
    print("To play the full game pay Rs 10 to Mr.Tushar Saxena")
elif first_choice in ['right','right']:
    third_choice=input("You have encountered a monster .Would you like to fight it?: ")
    if third_choice in ['yes','YES']:
            print("You Died")
    elif third_choice in ['no','NO']:
            print("He killed you before you could escape: ")
else:
    print("Invaild Choice")