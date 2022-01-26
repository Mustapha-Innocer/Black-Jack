class Player:
    def __init__(self, player_id, card1, card2):
        self.player_id = player_id
        self.status = None
        self.cards = [card1, card2]

    def collect(self, card):
        self.cards.append(card)

    def total(self):
        values = [card.value for card in self.cards]
        return sum(values)