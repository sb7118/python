'''rock ,paper , scissor '''
import random

#instructions
print('''
here are the instructions:
1= rock 
2= paper
3= scissor
''')

def logic():
    # computer logic
    if (computer == 1):
        print(' computer : rock')
    elif (computer == 2):
        print('computer : paper')
    elif (computer == 3):
        print('computer : scissor')

    # user logic
    if (user == 1):
        print('user : roxk')
    elif (user == 2):
        print('user : paper')
    elif (user == 3):
        print('user : scissor')

def gameLogic():
    ''' game logic'''
    if (user == 1 and computer == 1):
        print('its tie!')
    elif (user == 1 and computer == 2):
        print('you lose!')
    elif (user == 1 and computer == 3):
        print('you win!')

    if (user == 2 and computer == 1):
        print('you win!')
    elif (user == 2 and computer == 2):
        print('its tie!')
    elif (user == 2 and computer == 3):
        print('you lose!')

    if (user == 3 and computer == 1):
        print('you lose!')
    elif (user == 3 and computer == 2):
        print('you win!')
    elif (user == 3 and computer == 3):
        print('its tie!')


#loop
condition = True
while condition:
    user = int(input('enter your choice : '))
    computer = random.randint(1, 3)
    logic()
    gameLogic()

