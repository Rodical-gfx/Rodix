score = 0
while True:
    import random
    diff= int(input("CHOOSE DUFFUCULTY 1,2,3: ") )
    
    if diff>=1 and diff<=3:
        hidden = random.randrange(1, 10*diff)
        max= 10*diff
        #print(hidden)
        print("GUESS A NUMBER BETWEEN 0 AND "+ str(max)) 
        guess = int(input("Please enter your guess: "))
        if guess >= 0 and guess<=max:
            if guess == hidden:
                print("CORRECT!")
                score +=1 
            elif guess < hidden:
                print("Your guess is too low")
                guess = int(input("Please try again: "))
                if guess == hidden:
                    print("CORRECT!")
                    score +=1 
                elif guess < hidden:
                    print("Your guess is too low")
                    guess = int(input("Final try : "))
                    if guess == hidden:
                        print("CORRECT!")
                        score +=1 
                    else:
                    	print("FAIL. Answer is " + str(hidden)+ " \nYour Score is " + str(score))
                        #print("Your Score is " + str(score))
                else:
                    print("Your guess is too high")
                    guess = int(input("Final try : "))
                    if guess == hidden:
                        print("CORRECT!")
                        score +=1 
                    else:
                    	print("FAIL. Answer is " + str(hidden)+ " \nYour Score is " + str(score))
                        #print("Your Score is " + str(score))
            else:
                print("Your guess is too high")
                guess = int(input("Please try again: "))
                if guess == hidden:
                    print("CORRECT!")
                    score +=1 
                elif guess < hidden:
                    print("Your guess is too low")
                    guess = int(input("Final try : "))
                    if guess == hidden:
                        print("CORRECT!")
                        score +=1 
                    else:
                    	print("FAIL. Answer is " + str(hidden)+ " \nYour Score is " + str(score))
                        #print("Your Score is " + str(score))
                else:
                    print("Your guess is too high")
                    guess = int(input("Final try : "))
                    if guess == hidden:
                        print("CORRECT!")
                        score +=1 
                    else:
                    	print("FAIL. Answer is " + str(hidden)+ " \nYour Score is " + str(score))
                        #print("Your Score is " + str(score))
        else:
            print("please Enter a value within the Range to play")

    else:
            print("please Enter a value within the Range to play")