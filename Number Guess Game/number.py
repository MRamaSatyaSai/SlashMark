import random

def main():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while attempts < 10:
        guess = int(input("Make a guess: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try again! You guessed too low.")
        else:
            print("Try again! You guessed too high.")
    else:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    main()
