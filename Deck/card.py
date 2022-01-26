

class Card:
    def __init__(self,suit,rank):
        if isinstance(rank, tuple):
            self.suit = suit
            self.rank = rank[0]
            self.value = rank[1].value
        else:
            self.suit = suit
            self.rank = rank.name
            self.value = rank.value

    def __str__(self):
        return "{" + self.suit + " : " + self.rank + "}"