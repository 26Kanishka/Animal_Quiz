def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 1:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 2:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
guess4 = input("What is a baby hippo called? ")
check_guess(guess4, "calf")
guess5 = input("What is a group of wolves called? ")
check_guess(guess5, "Pack")
guess6 = input("What's name for a group of flamingos? ")
check_guess(guess6, "colony")

print("Your Score is "+ str(score))
