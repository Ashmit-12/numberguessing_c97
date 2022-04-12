import random

Num = random.randrange(1,9)

chanceCounter=0

print("the guessed number should be betweeen 1 and 9")
print("you have 5 chances to guess the number ")

while chanceCounter<5:
    guess=int(input("enter your guess : "))
    chanceCounter= chanceCounter + 1

    if guess < Num:
        print("oops ! too low, guess higher than ",guess," genius")

    if guess > Num:
        print("oops ! too high , guess lower than ",guess," genius")

    if guess == Num:
        print("you win!!")
        break

    if not chanceCounter < 5:
        print("you lost! hard luck next time")
        print("the number is ", Num)

