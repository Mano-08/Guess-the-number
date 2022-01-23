from random import randint


print("Hey there! Welcome to GUESS THE NUMBER challenge")
print("The rules:")
print("1.Enter a number between 0 and 1000")
print("2.COLD indicates that the number you guessed is below the actaul number.")
print("3.HOT indicates that the number you guess is above the actual number")
print("4.The no. of trials will be displayed and you can beat your Highscore.")
guess_no=input("Enter the number you guessed: ")
actual_no=randint(1,10**3)
count=0
c=1
while c==1:
    try:
        c=int(guess_no)
    except ValueError:
        if guess_no=='q':
            print('Exiting window. See you next time!')
            break
        else:
            print('Invalid Input')
            guess_no=input('Enter the number you guessed: ')
            c=1
    else:
        #add more interactive message box    
        if guess_no>actual_no:
            print("HOT!")
            count+=1
        elif guess_no<actual_no:
            print("COLD!")
            count+=1
        else:
            count+=1
            print("YAY! Congratulations!! You've guessed the correct number")

#add print no of trials statement here
#work on no of trials algorith ok?
            print("This is the number of Trials you've had: ", count)
            print("If you wanna try again, click y or click n to quit")
            d=input("Enter your choice:")
            if d=='y' or d=="Y":
                guess_no=int(input("Enter the number you guessed: "))
                actual_no=randint(1,10**3)
            elif d=='n' or d=='N':
                print("You clicked the exit option. Sad to see you go :(")
                #add exit window message here
                c=2
