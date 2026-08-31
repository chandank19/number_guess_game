import random
def play_game():
    secret = random.randint(1,100)
    attempts = 0
    while True:
        guess = int(input("Guess the number between 1 and 100 :"))
        attempts += 1 
        if guess == secret:
            print(f"Correct ! it took you {attempts} attempt")
            break
        elif guess < secret:
            print("Too Low !")
        else:
            print ("Too high !")

play_game()