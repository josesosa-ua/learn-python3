secret = 1337
attempt = -1
counter = 0

while attempt != secret:
    attempt = int(input("Guess the secret number: "))
    counter += 1
    if attempt < secret:
        print("Too low!")
    elif attempt > secret:
        print("Too high!")

print("Great! You guessed it in", counter, "attempts!")
