secret = 8

while True:
    guess = int(raw_input("Guess winning number - Enter number from 0 to 10: "))

    if guess == secret:
        print "you win - congratulations! It's number: " + str(guess)
        break

    elif guess > secret:
        print "Your guess is not correct, try with lower number: "

    elif guess < secret:
        print "your guess is not correct, try with higher number: "

print "Thank you for playing!"