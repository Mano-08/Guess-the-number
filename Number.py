from random import randint


print("Hey there! Welcome to GUESS THE NUMBER challenge")
print("The rules:/nEnter a number between 0 and 1000")
guess_no=int(input("Enter the number you guessed: "))
actual_no=randint(1,10**3)
c=1
while c:
    if guess_no>actual_no:
        print(