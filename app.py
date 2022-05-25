import random

rand = random.randint(0, 100)
end = False

user_guess = int(input("Enter an integer from 0 to 100: "))
while not end:
    if rand > user_guess:
        user_guess = int(input("Your guess is low, try again: "))
    elif rand < user_guess:
        user_guess = int(input("Your guess is too high, try again: "))
    elif rand == user_guess:
        print("Congratulations! Your guess is right.")
        end = True
    else:
        print("There is and error")
        end = True
