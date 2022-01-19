from random import randint


print("Hey there! Welcome to GUESS THE NUMBER challenge")
print("The rules:")
print("1.Enter a number between 0 and 1000")
print("2.COLD indicates that the number you guessed is below the actaul number.")
print("3.HOT indicates that the number you guess is above the actual number")
guess_no=int(input("Enter the number you guessed: "))
actual_no=randint(1,10**3)
c=1
while c==1:
    if guess_no>actual_no:
        print("HOT!")
    elif guess_no<actual_no:
        print("COLD!")
    else:
        print("YAY! Congratulations!! You've guessed the correct number")
        print("If you wanna try again, click y or click n to quit")
        d=input("Enter your choice:")
        
