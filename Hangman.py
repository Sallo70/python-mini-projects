import random

def play_hangman():
    # 1. List of 5 predefine Words
    words = ["python", "variable", "dictionary", "loop", "syntax", "function", "programming"]
    secret_word = random.choice(words)
    
    # 2. Track game state
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6 # 6 wrong guesses allowed
    
    print("Design by Suleman".upper())
    
    print("Welcome to Hangman!")
    
    # 3. Main Game Loop
    while wrong_guesses < max_attempts:
        # Show the current state of the gallows
        print(wrong_guesses)
        
        # Build the secret word hidden behind underscores
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        
        print("Word to guess: " + " ".join(display_word))
        print(f"Attempts remaining: {max_attempts - wrong_guesses}")
        print(f"Letters tried: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check if the player won
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: '{secret_word}'!")
            break
        
        # --- GET AND CHECK PLAYER INPUT ---    
        guess = input("\nGuess a letter (or type 'quit' to exit): ").lower().strip()
        
        # Check if the player wants to quit
        if guess == 'quit':
            print("\n👋 Thanks for playing! See you next time.")
            return  # Using 'return' exits the entire function immediately
        
        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.")
            continue
            
        # Check for duplicate guesses
        if guess in guessed_letters:
            print(f"⚠️ You already tried '{guess}'. Pick a different letter!")
            continue
        
            
        # Add guess to our record tracker
        guessed_letters.add(guess)
        
        # Evaluate the guess
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            wrong_guesses += 1
            
    # 4. Game Over (Triggered if the while loop finishes without a 'break')
    if wrong_guesses == max_attempts:
        print(wrong_guesses)
        print(f"\n💀 Game Over! You ran out of attempts. The word was: '{secret_word}'")

if __name__ == "__main__":
    play_hangman()