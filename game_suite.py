import tkinter as tk


def NG():
    """The main program for Number Guesser"""

    # Have user input maximum range for possible numbers to guess.
    max_range = input('Select the max range of possible numbers then press "ENTER"\n')

    # Check that user input a number and obtain new input if necessary.
    while not max_range.isdigit():
        max_range = input("Please enter a number\n")

    # Use random module to generate a number between 1 and users max range input.
    import random

    number = random.randint(1, int(max_range))

    # Define the guessing process and set a guesses counter to 1.
    def guessing(guesses=1):
        """Uses a recursive loop to aquire user input and provide feedback based on that input."""

        # Ask user for a guess number.
        guess = input('Guess a number then press "ENTER"\n')

        # Confirm user entered a number and obtain a new guess if necessary.
        while not guess.isdigit():
            guess = input("Please guess a number\n")

        # Convert guess from a string to an integer
        guess_int = int(guess)

        # Check if guessed number is the same as generated number.
        if guess_int == number:
            print(
                "Congratulations! It took you",
                guesses,
                "attempts to guess the number!\n",
            )

            # Ask if user would like to replay
            replay = input("Would you like to play again?\nY/N:")
            if replay.upper() == "Y":
                NG()
            else:
                print("Thank you for playing")

        # Provide feedback to user to guide them to the correct number and increase guess count.
        elif guess_int < number:
            print("My number is higher. Try again.\n")
            guessing(guesses + 1)
        elif guess_int > number:
            print("My number is lower. Try again.\n")
            guessing(guesses + 1)

    # Start the game.
    guessing()


def TTT():
    # Inspiration code from https://www.geeksforgeeks.org/implementation-of-tic-tac-toe-game/#

    # Set up the game board as a list.
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def print_board():
        """Prints the board so the players can track the game."""
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("--" + "|" + "---" + "|" + "--")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("--" + "|" + "---" + "|" + "--")
        print(board[6] + " | " + board[7] + " | " + board[8])

    def take_turn(player):
        """Handles the player input for turn flow."""

        # Notifies which players turn it is.
        print("\n" + player + "'s turn.")

        # Player picks a square.
        position = input("Choose a position from 1-9: ")

        # Checks that player input a valid option.
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        # Converts player input to index number for assignment to board list.
        position = int(position) - 1

        # Checks that input index is available and get a new input if necessary.
        while board[position] == "X" or board[position] == "O":
            position = input("Position already taken. Choose a different position: ")

            # Chekcs that player input a valid option.
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Invalid input. Choose a position from 1-9: ")

            # Converts player input to index number for assignment to board list.
            position = int(position) - 1

        # Assigns current player character to selected square.
        board[position] = player

        # Print the updated board.
        print_board()

    def check_game_over():
        """Checks the condition of the board to determ in game is over or should continue."""

        # Check for a win
        if (
            (board[0] == board[1] == board[2])
            or (board[3] == board[4] == board[5])
            or (board[6] == board[7] == board[8])
            or (board[0] == board[3] == board[6])
            or (board[1] == board[4] == board[7])
            or (board[2] == board[5] == board[8])
            or (board[0] == board[4] == board[8])
            or (board[2] == board[4] == board[6])
        ):
            return "win"

        # Check for a tie
        elif (
            (board[0] == "X" or board[0] == "O")
            and (board[1] == "X" or board[1] == "O")
            and (board[2] == "X" or board[2] == "O")
            and (board[3] == "X" or board[3] == "O")
            and (board[4] == "X" or board[4] == "O")
            and (board[5] == "X" or board[5] == "O")
            and (board[6] == "X" or board[6] == "O")
            and (board[7] == "X" or board[7] == "O")
            and (board[8] == "X" or board[8] == "O")
        ):
            return "tie"

        # Play continues
        else:
            return "play"

    # print the blank board.
    print_board()

    # Assign starting player character.
    current_player = "X"

    # Set game over to false to begin game loop.
    game_over = False

    # The main game loop.
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()

        # Check for win.
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True

        # Check for tie.
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True

        # Switch to the other player.
        else:
            current_player = "O" if current_player == "X" else "X"

    else:
        replay = input("\nPlay Again?\nY/N:")
        if replay.upper() == "Y":
            print("")
            TTT()
        else:
            print("Thank you for playing")


# Define Rock Paper Scissor 1 Player. Used for later recusion.
def RPS_1P():
    """The play loop for single player Rock, Paper, Scissors."""

    # Initialize replay with a default value.
    replay = ""

    # Obtain players choice.
    player = input("Choose Rock, Paper, or Scissor\n")

    # Covert players choice to upper case for later checks.
    player = player.upper()

    # Check that player entered a viable choice and obtain new choice if necessary.
    while player != "ROCK" and player != "PAPER" and player != "SCISSOR":
        player = input("Please select Rock, Paper, or Scissor\n")
        player = player.upper()

    # Use Random module to select CPU choice.
    import random

    throw = random.randint(1, 3)
    if throw == 1:
        opponent = "ROCK"
    if throw == 2:
        opponent = "PAPER"
    if throw == 3:
        opponent = "SCISSOR"
    print(f"Computer plays", opponent)

    # Check CPU choice agaist players choice and determine winner. If tie, play again automatically.
    if opponent == "ROCK" and player == "PAPER":
        replay = input("YOU WIN!\nPlay Again?\nY/N:")
    elif opponent == "PAPER" and player == "SCISSOR":
        replay = input("YOU WIN!\nPlay Again?\nY/N:")
    elif opponent == "SCISSOR" and player == "ROCK":
        replay = input("YOU WIN!\nPlay Again?\nY/N:")
    elif opponent == player:
        print("TIE! Go again!")
        RPS_1P()
    else:
        replay = input("YOU LOSE\nTry Again?\nY/N:")
    if replay.upper() == "Y":
        print("")
        RPS_1P()
    else:
        print("Thank you for playing")


# Define Rock Paper Scissor 2 Player. Used for later recusion.
def RPS_2P():
    """The play loop for two player Rock, Paper, Scissors."""
    print("HONOR RULES!\nNO PEAKING!\n")

    # Initialize replay with a default value.
    replay = ""

    # Obtain first players choice.
    player = input("Player 1, Choose Rock, Paper, or Scissor\n")

    # Covert players choice to upper case for later checks.
    player = player.upper()

    # Check that player entered a viable choice and obtain new choice if necessary.
    while player != "ROCK" and player != "PAPER" and player != "SCISSOR":
        player = input("Please select Rock, Paper, or Scissor\n")
        player = player.upper()

    # Obtain second players choice.
    opponent = input("Player 2, Choose Rock, Paper, or Scissor\n")

    # Covert players choice to upper case for later checks.
    opponent = opponent.upper()

    # Check that player entered a viable choice and obtain new choice if necessary.
    while opponent != "ROCK" and opponent != "PAPER" and opponent != "SCISSOR":
        opponent = input("Please select Rock, Paper, or Scissor")
        opponent = opponent.upper()

    # Check Player 1 choice agaist Player 2 choice and determine winner. If tie, play again automatically.
    if opponent == "ROCK" and player == "PAPER":
        replay = input("Player 1 WINS!\nPlay Again?\nY/N:")
    elif opponent == "PAPER" and player == "SCISSOR":
        replay = input("Player 1 WINS!\nPlay Again?\nY/N:")
    elif opponent == "SCISSOR" and player == "ROCK":
        replay = input("Player 1 WINS!\nPlay Again?\nY/N:")
    elif opponent == player:
        print("TIE! Go again!\n")
        RPS_2P()
    else:
        replay = input("Player 2 WINS!\nPlay Again?\nY/N:")
    if replay.upper() == "Y":
        print("")
        RPS_2P()
    else:
        print("Thank you for playing!")


def RPS():
    # Ask how many players will be playing the game.
    players = ""
    # Check that the user entered a valid response.
    while players != "ONE" and players != "TWO":
        players = input("Please select one or two players\n")

        # Convert input to upper case for later checks.
        players = players.upper()

    # Check number of players and start the game.
    if players == "ONE":
        RPS_1P()

    elif players == "TWO":
        RPS_2P()


def hangman():
    # Create dictionary of words from text file, keys == length of word, values == words of that length; all upper case.
    dict = {}
    with open("google-10000-english-usa.txt") as lib:
        for word in lib:
            word = word.rstrip()
            l = str(len(word))
            if l not in dict:
                dict[l] = [word.upper()]
            dict[l].append(word.upper())

    # Have user input desired length of word.
    word_len = input("How long of a word do you want?\n")

    # Check that user input a number.
    while not word_len.isdigit():
        word_len = input("Please enter a number.\n")

    # Check if the desired word length is in the dictionary.
    while 1 > int(word_len) or int(word_len) > 16:
        word_len = input("Please enter a number between 1 and 16.\n")

    # Build a bank of possible words based on the desiered length.
    word_bank = dict[word_len]

    # Convert word_len to integer for later comparisons.
    word_len = int(word_len)

    # Select a random word from the word bank.
    import random

    random_index = random.randint(0, len(word_bank))
    word = word_bank[random_index]

    # Convert word to a list of letters. Used to check user guesses.
    word_list = list(word)

    # Create variables to track correct and incorrect guesses.
    hanged_man = 0
    correct_guess = 0

    # Display blank spaces representing each letter in the word.
    word_display = list("_" * word_len)
    print(word_display)

    # Check if the word has been correctly guessed.
    while correct_guess != word_len:
        # Check if maximum number of incorrect guesses has been reached.
        if hanged_man == 6:
            replay = input(
                "GAME OVER\nThe word was " + str(word_list) + "\nTry Again?(Y/N)"
            )
            break

        else:
            # Have user input a letter.
            guess = input("Guess a letter.\n")

            # Check that the input is an alphabetic letter.
            while not guess.isalpha():
                guess = input("Please choose a letter.\n")

            # Check that only one letter was entered.
            while len(guess) > 1:
                guess = input("Please enter only one letter.\n")

            # Convert input into upper case.
            guess = guess.upper()

            # Check if guessed letter is in the generated word.
            if guess in word_list:
                # Reveal the placement of the guessed letter in the word to the user.
                for i in range(len(word_list)):
                    if word_list[i] in guess:
                        word_display[i] = guess
                        # Increment correct guess for game winning condition.
                        correct_guess += 1
                print(word_display)

            # Increment hanged_man for incorrect guesses and notify user of how many attmpts they have left.
            else:
                hanged_man += 1
                print(f"Your Hanged Man has", 6 - hanged_man, "chances left")

    # Check for winning condition and notify user.
    if correct_guess == word_len:
        replay = input("YOU WIN!\nPlay Again?(Y/N)")

    replay = replay.upper()
    if replay == "Y":
        hangman()
    else:
        print("Thank you for playing!")


# Launch Hangman upon button press
def HM():
    window.destroy()
    hangman()


# Launch Tic Tac Toe upon button press
def TicTacToe():
    window.destroy()
    TTT()


# Launch Rock, Paper, Sciccor upon button press
def rps():
    window.destroy()
    RPS()


# Launch Number Guesser upon button press
def NumGuess():
    window.destroy()
    NG()


# Create the main window
window = tk.Tk()
window.title("Game Suit")
frame = tk.Frame(master=window)

# Create the heading label
heading = tk.Label(text="Choose A Game", font=("Arial", 25))

# Create the button for Hangman
btn_HM = tk.Button(
    text="Hangman",
    master=frame,
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=5,
    command=HM,
)

# Create the button for Tic Tac Toe
btn_TTT = tk.Button(
    text="Tic Tac Toe",
    master=frame,
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=5,
    command=TicTacToe,
)

# Create the button for Rock, Paper, Sciccor
btn_RPS = tk.Button(
    text="Rock, Paper, Sciccors",
    master=frame,
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=5,
    command=rps,
)

# Create the button for Number Guesser
btn_NG = tk.Button(
    text="Number Guesser",
    master=frame,
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=5,
    command=NumGuess,
)


# Place the heading and buttons into the window grid
heading.grid(row=0)
frame.grid(row=1)
btn_HM.grid(row=1, column=0)
btn_TTT.grid(row=1, column=1)
btn_RPS.grid(row=2, column=0)
btn_NG.grid(row=2, column=1)

window.mainloop()
