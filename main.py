import random
import requests
import os

game_running = True
game_finished = False
guessed_chars = ''
letters = 'abcdefghijklmnopqrstuvwxyz'
status = ''


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw_man(stage):
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


while game_running:
    clear_screen()
    print('Welcome to Hangman!')
    online_words = requests.get(
        'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain').content.decode(
        'utf-8').split()
    word = str(online_words[random.randint(0, len(online_words))].lower())
    guess_blank = '_' * len(word)
    stage = 0
    while not game_finished:
        if '_' not in guess_blank:
            print('You win!')
            break
        if status != '':
            print(status)
        print('Current guess: ' + guess_blank)
        draw_man(stage)
        guess = input('What is your guess? ').lower()
        if len(guess) == 1:
            if guess in letters:
                if guess not in guessed_chars:
                    if guess in word:
                        for i in [pos for pos, char in enumerate(word) if char == guess]:
                            guess_array = list(guess_blank)
                            guess_array[i] = guess
                            guess_blank = ''.join(guess_array)
                    else:
                        stage += 1
                        status = 'Nope!'
                    guessed_chars += guess
                else:
                    status = 'You\'ve already tried that!'
            else:
                status = 'Letters only please!'
        else:
            status = 'One at a time please!'

        if stage == 6:
            draw_man(stage)
            print('\n\rHe\'s dead Jim!\n\rThe word was: ' + word + '\n\r')
            break
        clear_screen()

    if input('Do you want to play again (y/n)? ').lower() == 'n':
        status = ''
        break
