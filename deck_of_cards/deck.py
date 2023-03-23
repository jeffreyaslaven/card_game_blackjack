from deck_of_cards.card import Card
from random import randrange

"""
Representation of a deck of cards
"""
class Deck(Card):
    def __init__(self) -> None:
        self.possible_suit = ['hearts', 'clubs', 'spades', 'diamonds']
        self.possible_number = range(1, 14)
        self.deck = []
    
    """
    Create a single deck of cards
    """
    def create_deck_of_cards(self) -> None:
        return [Card(suit, number) for number in self.possible_number for suit in self.possible_suit]

    """
    Create multiple decks of cards
    """    
    def create_multiple_decks(self, number_of_decks: int) -> None:
        single_deck_of_cards = self.create_deck_of_cards()
        for _ in range(number_of_decks):
            self.deck  = self.deck + single_deck_of_cards.copy()
    

    """
    Draw a random card from the deck of cards
    """
    def draw_card(self) -> Card:
        size_of_deck = len(self.deck)
        random_card_position = randrange(0, size_of_deck)
        return self.deck.pop(random_card_position)
    
    """
    Check if deck is empty and thus game is over
    """
    def is_deck_empty(self) -> bool:
        return len(self.deck) == 0
    
    """
    Due to Jack, Queen, King, Ace being strings
    Convert this for the user if number as follows to follow conventional card number values:
    1: Ace
    11: Jack
    12: Queen
    13: King
    """
    def check_card_number_value(self, card: Card):
        card_mappings = {1: 'ace', 11: 'jack', 12: 'queen', 13: 'king'}
        number = card_mappings.get(card.number, None)
        if number is not None:
            return number
        else:
            return card.number

    
    if __name__ == '__main__':
        pass

