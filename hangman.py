import random
from pathlib import Path

map = [[' ','O',' '],
       ['/','|','\\'],
       ['/',' ','\\']]
words_file = open("hangman_words.txt", 'r')
read_file = words_file.read().splitlines()

playagain = 'yes'

def word_choice():
    word = random.choice(read_file)
    return word

if playagain == 'yes':
    word = word_choice()

output = []
for i in word:
    output.append(i)
display = []
for i in range(len(output)):
    sub = '_'
    display.append(sub)
print(display)


def error(error_count):
    if error_count == 1:
        for x in map[0]:
            print(x, end='')
            print()

    if error_count == 2:
        for x in map[0]:
            print(x, end='')
        print()
        print(map[1][0])
        print()

    if error_count == 3:
        for x in map[0]:
            print(x, end='')
        print()
        for x in range(2):
            print(map[1][x], end='')
        print()

    if error_count == 4:
        for x in map[0]:
            print(x, end='')
        print()
        for x in map[1]:
            print(x, end='')
        print()

    if error_count == 5:
        for x in map[0]:
            print(x, end='')
        print()
        for x in map[1]:
            print(x, end='')
        print()
        print(map[2][0])

    if error_count == 6:
        for x in map[0]:
            print(x, end='')
        print()
        for x in map[1]:
            print(x, end='')
        print()
        for x in map[2]:
            print(x, end='')
        print()

def game():
    count = 0
    used = []
    while display != output:
        answer = input("Enter a letter: ")
        used_letter = answer
        used.append(used_letter)
        if answer in output:
            index_o = output.index(answer)
            display.pop(index_o)
            display.insert(index_o, answer)
            print(display)
            print(f"Used letters: {used}")
        else:
            count += 1
            error(count)
            if count != 6:
                print(display)
                print(f"Used letters: {used}")
                
    else:
        if display == output:
            print('You won!!')
            playagain = input('Would you like to play again? (yes or no): ').lower()

    if count == 6:
        print('You lost!')
        playagain = 'no'
        playagain = input('Would you like to play again? (yes or no): ').lower()
    return playagain
playagain = game()
