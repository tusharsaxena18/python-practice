player = False
print("Do you want to play again")
end = input()
if end  in ['y']:
    player=False
else:
    player=True
    print("Press any key to exit: ")
    end=input("")
    if end in ['y']:
        exit()
    else:
        exit()