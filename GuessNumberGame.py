import random as r

print("-- Guess the Number --")
print()

start = int(input("Enter Starting Range :" ))
end = int(input("Enter Ending Range :" ))
random_number = r.randint(start, end)

while True:
    guess_number = int(input("Guess Number : "))

    if guess_number > random_number:
        print("Try choosing lower number...")
    elif guess_number < random_number:
        print("Try choosing higher number...")
    else:
        print("The Correct Number was", guess_number)
        print("Congratulations... You Guessed correct number")
        break