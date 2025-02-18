import random

correct_number = random.randint(0, 1000)

level = input("Select a game level(1: normal, 2: hard):  ")
if level != "1" and level != "2":
    print("Not exsistant this level!")
    exit()

chance = 10 if level == "1" else 5

count = 0
while count < chance:
    try:
        print(f"Rest of your chance ({chance - count})")
        guess = int(input("your prediction: "))
        count += 1
        if guess == correct_number:
            print(f"Correct!record: {count} time")
        elif guess < correct_number:
            print("more large")
        else:
            print("more small")
    except ValueError:
        print("Invalid input. plese input number")

if count == chance:
    print(f"Oops! Correct number is {correct_number}")