import random
playing = True
number = random.randint(1,100)

if number%2==0:
    print("HINT!: I have chosen an even number from 1 to 100! take a guess and see if you can find it!")
else:
    print("HINT!: I have chosen an odd number from 1 to 100! take a guess and see if you can find it!")
print("the game will end only if u input the correct answer!")

attempts=0
while playing:
    guess = int(input("Give me your best guess! \n"))
    attempts+=1
    if number == guess:
        print("YOU WIN THE GAME!!")
        print(" The number",number,"is guessed in",attempts,"attempts!")
        break

    else:
        print("Your guess isnt quite right, try again. \n")
        if guess>number:
            print("Guess a smaller number")
        else:
            print("Guess a bigger number")
