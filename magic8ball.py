"""
Magic 8 Ball program
"""

import time
import random as rand
import asciiArt as art

# Loads answers from 'answers.txt' file:
answers = []
with open('answers.txt') as a:
    for line in a:
        answers.append(line)

question = ""

# Prints the welcome art:
art.welcome()

while True:
    question = input('Enter a qusetion (or type "Quit" to Exit): ')
    if question == 'Quit':
        break
    art.processing()
    time.sleep(1)
    print()

    # Getting and printing random answer from the list:
    ansNumber = rand.randint(0, len(answers))
    print('~' * (len(answers[ansNumber])-1))
    print(answers[ansNumber][:-1])
    print('~' * (len(answers[ansNumber])-1))
    print()