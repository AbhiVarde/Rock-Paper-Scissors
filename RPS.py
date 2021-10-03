import random

def play():
    print("\n Welcome to Rock-paper-scissors game !!")
    print("let's play !")
    user = input("\n What's your choice ?\n 'r' for Rock\n 'p' for Paper\n 's' for Scissors\n Pick Your Choice : ")
    user = user.lower()
    print('\n')
    computer = random.choice(['r','p','s'])

    if user == computer:
        return ("It's tie. You and the computer both have chosen {}.\n".format(computer))
    if is_win(user,computer):
        return ("You won ! You chose {} and the computer chose {}.\n".format(user,computer))

    return ("You lose ! You chose {} and the computer chose {}.\n".format(user,computer))

def is_win(player,opponent):
    if (player == 'r' and opponent =='s') or (player =='s' and opponent =='p') or (player =='p' and opponent =='r'):
        return True
    return False

if __name__ == '__main__':
    print(play())
