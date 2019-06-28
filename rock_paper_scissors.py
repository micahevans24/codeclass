# Here is a short python program... try it out!
import time          # includes a module named time
import random        # a random module

name = input('Hi... what is your name? ')   
print('')

if name == 'Matt' or name == 'Matthew':
    print('I\'m "offline." Try later.')

elif name == 'Lucas':                            
    print('Lukey Luke?!')
    time.sleep(.5)             
    print('No?')
    time.sleep(.5)
    print('Meh.')

else:                   
    print('Welcome,', name)

choice = input('Pick rock, paper, or scissors.')
print('')



if choice == 'rock' or 'Rock':
    print('You chose rock. I chose paper - I win!')

elif choice == 'paper' or 'Paper':
    print('You chose', your_choice. 'I chose,' , 'my_choice' scissors - I win!')

elif choice == 'scissors' or 'Scissors':
    print('You chose scissors. I chose rock - I win!')

else:
    print("Oops! That is not allowed - Game over!")