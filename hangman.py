import random

def choose_state():
    """
    Randomly selects a U.S. state from a predefined list.

    Returns:
        str: The name of a randomly selected U.S. state in lowercase.
    """
    states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware",
        "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky",
        "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
        "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey", "new mexico",
        "new york", "north carolina", "north dakota", "ohio", "oklahoma", "oregon", "pennsylvania",
        "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah", "vermont",
        "virginia", "washington", "west virginia", "wisconsin", "wyoming"
    ]
    return random.choice(states)

def display_state(state, guessed_letters):
    """
    Creates a string representation of the state with underscores for unguessed letters.

    Parameters:
        state (str): The U.S. state to guess.
        guessed_letters (list): Letters the player has guessed so far.

    Returns:
        str: State name with guessed letters revealed and others as underscores.
    """
    displayed_state = ""
    for letter in state:
        if letter in guessed_letters:
            displayed_state += letter
        else:
            displayed_state += "_"
    return displayed_state

def hangman():
    """
    Runs the Hangman game for guessing U.S. states.
    
    The player has 6 attempts to guess letters in the state name.
    The game ends when the player guesses the state correctly or runs out of attempts.
    """
    state = choose_state()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman - U.S. States Edition!")
    print("Try to guess the name of a U.S. state.")
    print(display_state(state, guessed_letters))  # Show initial underscores

    while True:
        guess = input("Guess a letter: ").lower()  # Convert input to lowercase for consistency

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in state:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
            print("Attempts left:", attempts)
            if attempts == 0:
                print("Sorry, you lose. The state was:", state.title())
                break

        # Show the current state of the word
        displayed_state = display_state(state, guessed_letters)
        print(displayed_state)

        # Check if the player has guessed the whole state
        if "_" not in displayed_state:
            print("Congratulations, you guessed the state!")
            break

# Start the game
hangman()
