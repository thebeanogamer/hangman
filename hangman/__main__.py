from os import name, system
from random import randint
from string import ascii_lowercase as letters
from typing import List

import requests

from hangman.stages import stages


def get_word_list() -> List[str]:
    words_url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co'
    resp = requests.get(words_url)
    return resp.text.split()


def get_random_word(word_list: List[str]) -> str:
    rand_index = randint(0, len(word_list))
    return word_list[rand_index]


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def draw_man(stage_num):
    print(stages[stage_num])


def get_blanked_word(word: str, guessed_letters: str) -> str:
    blanked = ''

    for character in word:
        if character in guessed_letters:
            blanked += character
        else:
            blanked += '_'

    return blanked


def is_word_guessed(word: str, guessed_letters: str) -> bool:
    for character in word:
        if character not in guessed_letters:
            return False
    return True


def start_game():
    word_list = get_word_list()

    game_finished = False

    while not game_finished:
        clear_screen()
        print('Welcome to Hangman!')

        word = get_random_word(word_list)
        start_round(word)

        choice = input('Do you want to play again? (y/N): ')
        if not choice.lower().startswith('y'):
            game_finished = True


def start_round(word: str):
    round_finished = False
    guessed_chars = ''
    hanged_stage = 0

    while not round_finished:
        guess_blank = get_blanked_word(word, guessed_chars)

        print("You've tried: " + guessed_chars)
        print('Current guess: ' + guess_blank)
        draw_man(hanged_stage)
        guess = input('What is your guess? ').lower()

        clear_screen()

        if not len(guess) == 1:
            print('One at a time please!')
        elif guess not in letters:
            print('Letters only please!')
        elif guess in guessed_chars:
            print("You've already tried that!")
        else:
            if guess not in word:
                hanged_stage += 1
                print('Nope!')
            guessed_chars += guess

            if hanged_stage == 6:
                draw_man(hanged_stage)
                print("He's dead Jim!")

                round_finished = True
            elif is_word_guessed(word, guessed_chars):
                draw_man(hanged_stage)
                print('You won!')

                round_finished = True

    print('The word was: ' + word)

if __name__ == "__main__":
    start_game()
