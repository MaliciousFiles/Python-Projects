from random import choice, randint


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


class card:
    def __init__(self, suit, number):
        if suit not in ['Spade','Club','Heart','Diamond', 'Joker']:
            raise DeckError('Invalid suit: %s' % suit)

        if number is not int:
            raise DeckError('number must be an integer')

        if not 0 < number < 14:
            raise DeckError('Invalid number: %s' % number)

        j = True

        long_suit = suit.capitalize()

        if suit == 'Joker':
            j = False
            self.name = 'J'
            self.long_name = 'Joker'

        if long_suit[-1]!='s':
            long_suit+='s'

        suit = suit[0].lower()
        self.value = number
        long_number = number

        if number == 1:
            number='A'
        if number == 11:
            number='J'
        if number == 12:
            number='Q'
        if number == 13:
            number='K'
        if long_number == 1:
            long_number='Ace'
        if long_number == 11:
            long_number='Jack'
        elif long_number == 12:
            long_number='Queen'
        elif long_number == 13:
            long_number='King'
        if j:
            self.long_name = str(long_number) + ' of ' + long_suit
            self.name = str(number) + suit
        self.number = number
        self.suit = suit

    def __repr__(self):
        return self.name


class deck:
    def __init__(self, jokers=False):
        self.cards=[]

        x=0
        for suit in ['spade','club','heart','diamond']:
            for number in range(1, 14):
                self.cards += str(number)[0]
                j = card(suit, number)
                self.cards[(number-1)+(13*x)]=j
            x+=1

        if jokers:
            self.cards += '1'
            self.cards[-1] = card('Joker',0)
            self.cards+='1'
            self.cards[-1] = card('Joker',0)

    def draw(self, numofcards):
        if numofcards > len(self.cards):
            raise DeckError('You asked for %s cards, but the deck only contains %s' % (numofcards, len(self.cards)))

        self.drawn_cards=[]
        for x in range(0, numofcards):
            self.drawn_cards += '1'

            self.drawn_cards[x] = self.cards.pop(randint(0,len(self.cards)-1))

        return self.drawn_cards

        def __repr__(self):
            return self.drawn_cards

    def __repr__(self):
        return str(self.cards)

c = card('Spade', 'oof')
print(c)
