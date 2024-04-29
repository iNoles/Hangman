import random

def choose_state():
    states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware",
              "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky",
              "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
              "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey", "new mexico",
              "new york", "north carolina", "north dakota", "ohio", "oklahoma", "oregon", "pennsylvania",
              "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah", "vermont",
              "virginia", "washington", "west virginia", "wisconsin", "wyoming"]
    return random.choice(states)

def display_state(state, guessed_letters):
    displayed_state = ""
    for letter in state:
        if letter in guessed_letters:
            displayed_state += letter
        else:
            displayed_state += "_"
    return displayed_state

def hangman():
    state = choose_state()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman - U.S. States Edition!")
    print("Try to guess the name of a U.S. state.")
    print(display_state(state, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

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

        displayed_state = display_state(state, guessed_letters)
        print(displayed_state)

        if "_" not in displayed_state:
            print("Congratulations, you guessed the state!")
            break

hangman()
