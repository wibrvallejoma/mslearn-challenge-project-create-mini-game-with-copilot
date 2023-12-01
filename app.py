# write a run rock, paper, scissors game that receives user input from the console and plays against the computer
# choose to continue playing

import random

def play():
    continue_playing = True

    while continue_playing:
        choices = ['r', 'p', 's']
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        
        if user not in choices:
            print('Invalid input')
            continue

        computer = random.choice(choices)

        print(f"Computer chose {computer}")

        if user == computer:
            print('It\'s a tie')
        elif is_win(user, computer):
            print('You won!')
        else:
            print('You lost!')

        continue_playing = input("Do you want to continue playing? (y/n) ").lower() == 'y'
    return 'Bye!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    return False

screen = '''
Welcome to Rock, Paper, Scissors!
'''
print(screen)
print(play())
