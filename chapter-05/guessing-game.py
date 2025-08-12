secret = 1337
attempt = -1
counter = 0

while (attempt := int(input("Guess the secret number: "))) != secret:
    if attempt < secret:
        print("Too low!")
    elif attempt > secret:
        print("Too high!")
    counter += 1

print("Great! You guess it in {} attempts! {}".format(counter, "Yay!"))
