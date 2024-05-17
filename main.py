import random
print("guess the sports:")
words = ['cricket', 'football', 'baseball', 'tennis']
secret_word = random.choice(words)
print(f"The secret word has {len(secret_word)} letters.")
incorrect_guesses = 0
guessed_letters = []
while incorrect_guesses < 6 and set(secret_word) != set(guessed_letters):
    guess = input("Guess a letter: ")
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess not in secret_word:
        incorrect_guesses += 1
        print(f"Sorry, {guess} is not in the word.")
    else:
        print(f"Good guess! {guess} is in the word.")
if incorrect_guesses == 6:
    print("Dobara kohsish Karein")
else:
    print("!!!!!!!!!!!!!Congratulations you won the game!!!!!!!!!!!!!!!!!!!!!!!!!!")
