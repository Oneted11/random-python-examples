import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number greater than zero next time. ")
        quit()
else:
    print("please type a number next time. ")
    quit()
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type number next time.")
        continue  # bring us back to the beginning of our while loop
    if user_guess == random_number:
        print("Congratulations !! You got it")
        break  # once the user gueses correctly we end/break out of the loop

    elif user_guess > random_number:
        print('go lower')
    else:
        print('go higher')

print("In only", guesses, "guesses")
# print(random_number)
