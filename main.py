from games.blackjack import Blackjack

"""
Main - Run file to play Blackjack
"""
def main():
    game = Blackjack()
    game.play_game()
    while True:
        user_choice = input('Do you want to play again? "Y" for yes "N" for No: ')
        if user_choice.lower() == 'y':
            game.play_game()
        elif user_choice.lower() == 'n':
            break
        else:
            print('Invalid choice. Please type either type "Y" or "N"')

if __name__ == '__main__':
    main()
