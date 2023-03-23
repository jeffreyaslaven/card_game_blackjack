from deck_of_cards import deck
from deck_of_cards import card
from time import sleep

"""
Logic for the Blackjack game
"""
class Blackjack(deck.Deck):
    def __init__(self) -> None:
        self.player_count = 0
        self.cpu_count = 0
        self.dealer_hidden_card: card.Card = card.Card('', 0)
        self.player_bust = False
        self.cpu_bust = False
    
    def play_game(self):
        print('_________________________________________________')
        print('\n')
        print('Welcome to BlackJack!')
        print('\n')
        print('_________________________________________________')

        number_of_decks = 0
        while True:
            number_of_decks = input('How many decks of cards do you want: ')
            if number_of_decks.isdigit() == False:
                print('That is not a valid number, please enter a valid number')
            elif number_of_decks.isdigit() == True and int(number_of_decks) < 1:
                print('That is not a valid number, please pick a number greater than 0')
            else:
                break
        
        print('You will have ' + number_of_decks + ' decks.')
        print('Lets start the game: ')
        print('_________________________________________________')
        
       
        game = deck.Deck()
        game.create_multiple_decks(int(number_of_decks))

        """
        Check status of hand to see if it is less than 21
        If hand is 21 return True
        Else return False
        """
        def core_logic(hand_count: int) -> bool:
            if hand_count <= 21:
                return True
            else:
                return False
        
        """
        Check status of deck to see if deck has at least two cards
        If it does return True
        Else return False
        """
        def does_deck_have_at_least_two_cards() -> bool:
            if len(game.deck) >= 2:
                return True
            else:
                return False

        """
        Convert values from card to equal values relevant to Blackjack
        """
        def blackjack_conversion_values(card_value: int) -> int:
            if card_value > 10:
                return 10
            else:
                return card_value
        
        """
        Convert an Ace to 11 or 1
        """
        def blackjack_convert_ace(card_value: int, is_not_cpu=True) -> int:
            if card_value == 1 and is_not_cpu:
                while True:
                    user_input = input('You drew an Ace, do you want it to be 1 or 11: ')
                    if not user_input.isdigit():
                        print('Invalid value, please enter a 1 or 11')
                    elif user_input.isdigit():
                        if int(user_input) == 1 or int(user_input) == 11:
                            return int(user_input)
                        else:
                            print('Invalid value, please enter a 1 or 11')
            elif card_value == 1 and not is_not_cpu:
                if self.cpu_count + 11 == 17:
                    return 11
                elif self.cpu_count + 1 == 17:
                    return 1
                elif self.cpu_count + 11 > 21:
                    return 1
                elif self.cpu_count + 11 <= 21:
                    return 11
            else:
                return card_value

        """
        First turn with CPU
        """
        def phase_one() -> None:
            print('Dealers turn!')
            dealer_card = game.draw_card()
            self.cpu_count = self.cpu_count + blackjack_convert_ace(blackjack_conversion_values(dealer_card.number), False)
            print('The dealer drawed a ' + str(game.check_card_number_value(dealer_card)) + ' of ' + str(dealer_card.suit))
            print('And an additional card facedown')
            print('The dealer count you can see is: ' + str(self.cpu_count))
            dealer_card_two = game.draw_card()
            self.cpu_count = self.cpu_count + blackjack_convert_ace(blackjack_conversion_values(dealer_card_two.number), False)
            self.dealer_hidden_card = dealer_card_two

        """
        The players turn
        """
        def phase_two() -> None:
            player_choice = 'h'
            print('Your turn!')
            while player_choice:
                if game.is_deck_empty():
                    print('The game is over, the deck is empty!')
                    break
                current_state = core_logic(self.player_count)
                if current_state:
                    player_choice = input('Hit or stay? Type "H" for Hit and "S" for Stay: ')
                    if player_choice.lower() == 'h':
                        player_card = game.draw_card()
                        self.player_count = self.player_count + blackjack_convert_ace(blackjack_conversion_values(player_card.number))
                        print('The dealer drew a ' + str(game.check_card_number_value(player_card)) + ' of ' + str(player_card.suit))
                        print('Your new count is: ' + str(self.player_count))
                    elif player_choice.lower() == 's':
                        print('Your current count is: ' + str(self.player_count))
                        break
                    else:
                        print('Not a valid value.')
                else:
                    print('You bust!')
                    self.player_bust = True
                    break
                    
        """
        CPU's second turn
        """
        def phase_three() -> None:
            if not game.is_deck_empty() and not did_player_lose_hand:        
                print('Dealers turn!')
                print('The dealer flips over their card.')
                print('Their hidden card was a ' + str(game.check_card_number_value(self.dealer_hidden_card)) + ' of ' + str(self.dealer_hidden_card.suit))
                print('The dealers count is: ' + str(self.cpu_count))
                while True:
                    if self.cpu_count < 17:
                        print('Dealer draws a card')
                        dealer_card = game.draw_card()
                        print('It\'s a ' + str(game.check_card_number_value(dealer_card)) + ' of ' + str(dealer_card.suit))
                        self.cpu_count = self.cpu_count + blackjack_convert_ace(blackjack_conversion_values(dealer_card.number), False)
                    elif self.cpu_count == 17:
                        print('Dealer has 17 and must stand.')
                        break
                    elif self.cpu_count == 21:
                        print('Dealer has 21!')
                        break
                    elif self.cpu_count > 21:
                        print('Dealer Bust!')
                        self.cpu_bust = True
                        break
                    else:
                        break

        """
        Check to see who won the hand of Blackjack
        """
        def who_won():
            if not self.player_bust and self.cpu_bust:
                print('Congrats you won that hand!')
            elif self.player_bust and not self.cpu_bust:
                print('Sorry! You lost that hand!')
            elif self.player_count == self.cpu_count:
                print('You push! No one wins!')
            elif self.player_count > self.cpu_count:
                print('Congrats you win the hand!')
            elif self.player_count < self.cpu_count:
                print('You lost that hand. Better luck next time!')

        while True:
            did_player_lose_hand = False
            if does_deck_have_at_least_two_cards():
                phase_one()
                print('_________________________________________________')
                phase_two()
                if not self.player_bust:
                    print('_________________________________________________')
                    phase_three()
                    print('_________________________________________________')
                    who_won()
                    print('_________________________________________________')
                    sleep(5)
                else:
                    print('_________________________________________________')
                self.cpu_count = 0
                self.player_count = 0
                self.dealer_hidden_card: card.Card = card.Card('', 0)
                self.cpu_bust = False
                self.player_bust = False
            else:
                print('The deck ran out of cards!')
                break

    if __name__ == '__main__':
        pass