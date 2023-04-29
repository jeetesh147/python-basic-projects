# Hangman Game :
import random
words = ['python', 'java', 'javascript', 'ruby', 'php', 'csharp', 'swift']
word = random.choice(words)
hidden_word = ['_'] * len(word)
guessed_letters = []

# keep track of the number of incorrect guesses
num_guesses = 0
max_guesses = 6

# main game loop
while True:
    print(' '.join(hidden_word))
    guess = input('Guess a letter: ').lower()
    if guess in guessed_letters:
        print('You already guessed that letter!')
        continue

    # add the letter to the list of guessed letters
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

        # check if the player has won
        if '_' not in hidden_word:
            print('Congratulations, you win!')
            break
    else:
        # increment the number of incorrect guesses
        num_guesses += 1
        print('Incorrect guess!')
        if num_guesses == max_guesses:
            print('Sorry, you lose!')
            print(f'The word was {word}.')
            break
