import random
import requests
import os

gameRunning = True
gameFinished = False
guessedChars = ''
letters = 'abcdefghijklmnopqrstuvwxyz'
status = ''


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pickWord():
    onlineWords = requests.get(
        'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain').content.decode(
        "utf-8").split()
    return str(onlineWords[random.randint(0, len(onlineWords))].lower())


def drawMan(stage):
    if stage == 0:
        print('''
             _________
             |/      |
             |      
             |      
             |       
             |      
             |
            _|___
            ''')
    elif stage == 1:
        print('''
             _________
             |/      |
             |      (_)
             |       
             |       
             |      
             |
            _|___''')
    elif stage == 2:
        print('''
             _________
             |/      |
             |      (_)
             |       |
             |       |
             |      
             |
            _|___''')
    elif stage == 3:
        print('''
             _________
             |/      |
             |      (_)
             |      \|
             |       |
             |      
             |
            _|___''')
    elif stage == 4:
        print('''
             _________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      
             |
            _|___''')
    elif stage == 5:
        print('''
             _________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / 
             |
            _|___''')
    elif stage == 6:
        print('''
             _________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / \\
             |
            _|___''')

def createGuessed(word):
    return '_' * len(word)


def gameLoop(word):
    global guessBlank
    global stage




while gameRunning:
    clearScreen()
    print('Welcome to Hangman!')
    word = pickWord()
    guessBlank = createGuessed(word)
    stage = 0
    while not gameFinished:
        if '_' not in guessBlank:
            print("You win!")
            break
        if status != '':
            print(status)
        print("Current guess: " + guessBlank)
        drawMan(stage)
        guess = input("What is your guess? ").lower()
        if len(guess) == 1:
            if guess in letters:
                if guess not in guessedChars:
                    if guess in word:
                        for i in [pos for pos, char in enumerate(word) if char == guess]:
                            guessArray = list(guessBlank)
                            guessArray[i] = guess
                            guessBlank = "".join(guessArray)
                    else:
                        stage += 1
                        status = ("Nope!")
                    guessedChars += guess
                else:
                    status = ("You've already tried that!")
            else:
                status = ("Letters only please!")
        else:
            status = ("One at a time please!")

        if stage == 6:
            drawMan(stage)
            print("\n\rHe's dead Jim!\n\rThe word was: " + word + "\n\r")
            break
        clearScreen()

    if input("Do you want to play again (y/n)? ").lower() == "n":
        status = ''
        break
