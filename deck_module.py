from random import choice, randint


# Custom error
class DeckError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'DeckError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'


# The card class
class card:
    # When the class is created:
    def __init__(self, suit, number):
        # Validate that the suit is an actual suit
        if suit.lower() not in ['spade','club','heart','diamond', 'joker']:
            raise DeckError('Invalid suit: %s' % suit)

        # Make sure number is an integer
        if number is not int:
            raise DeckError('number must be an integer')

        # Make sure number is in range
        if not 0 < number < 14:
            raise DeckError('Invalid number: %s' % number)

        # The suit isn't joker by default
        j = True

        # Make long suit name capitalized
        long_suit = suit.capitalize()

        # If the suit is a joker...
        if suit == 'Joker':
            j = False
            self.name = 'J'
            self.long_name = 'Joker'

        # Add an s to the end of all long suits with no s
        if long_suit[-1]!='s':
            long_suit+='s'

        # set suit to the first letter of suit lowercase
        suit = suit[0].lower()

        # Set the value to number and long number to number
        self.value = number
        long_number = number

        # Assign Ace, Jack, etc. to cards 1, 11, etc.
        if number == 1:
            number='A'
        elif number == 11:
            number='J'
        elif number == 12:
            number='Q'
        elif number == 13:
            number='K'

        # Do the same as above but with long number
        if long_number == 1:
            long_number='Ace'
        elif long_number == 11:
            long_number='Jack'
        elif long_number == 12:
            long_number='Queen'
        elif long_number == 13:
            long_number='King'

        # Set name and long name if the card is not a joker
        if j:
            self.long_name = str(long_number) + ' of ' + long_suit
            self.name = str(number) + suit

        # Set the number and suit
        self.number = number
        self.suit = suit

    def __repr__(self):
        return self.name


# Deck class
class deck:
    def __init__(self, jokers=False):
        # Set cards as empty list
        self.cards=[]

        x = 0

        # Do for every suit
        for suit in ['spade','club','heart','diamond']:
            # Do for every number
            for number in range(1, 14):
                # Add a card to the deck
                self.cards += str(number)[0]
                j = card(suit, number)
                self.cards[(number - 1) + (13 * x)] = j
            x+=1

        # Add a joker to deck if jokers is true
        if jokers:
            self.cards += '1'
            self.cards[-1] = card('Joker',0)
            self.cards+='1'
            self.cards[-1] = card('Joker',0)

    # Draw a certain number of cards
    def draw(self, numofcards):
        # Make sure numofcards is an integer
        if numofcards is not int:
            raise DeckError('numofcards must be an integer')

        # Make sure the number of cards is a valid amount
        if numofcards > len(self.cards):
            raise DeckError('You asked for %s cards, but the deck only contains %s' % (numofcards, len(self.cards)))

        # Set drawn_cards to a list
        self.drawn_cards=[]

        # Cycle through until the number of cards is reached
        for x in range(0, numofcards):
            self.drawn_cards += '1'

            self.drawn_cards[x] = self.cards.pop(randint(0,len(self.cards)-1))

        return self.drawn_cards

        def __repr__(self):
            return self.drawn_cards

    def __repr__(self):
        return str(self.cards)
