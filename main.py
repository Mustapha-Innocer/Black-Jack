from Deck.deck import Deck
from Player.player import Player
from Player.player_status import PlayerStatus

deck = Deck()
deck.shuffle()


def create_players(number):
    player_list = []
    for player_id in range(number):
        player = Player(player_id, deck.deal_card(), deck.deal_card())
        player_list.append(player)
    return player_list


def hit(player):
    player.status = PlayerStatus.HIT
    player.collect(deck.deal_card())


def stick(player):
    player.status = PlayerStatus.STICK


def go_bust(player):
    player.status = PlayerStatus.GO_BUST


def play(active_players):
    stick_player = []
    exactly_21_players = []
    while len(active_players) > 0:
        for player in active_players:
            if player.total() < 17:
                hit(player)
                print(str(player.player_id) + ": " + player.status.name + "----" + str(player.total()))
            elif player.total() > 21:
                go_bust(player)
                active_players.remove(player)
                print(str(player.player_id) + ": " + player.status.name + "----" + str(player.total()))
            elif player.total() >= 17:
                stick(player)
                stick_player.append(player)
                players.remove(player)
                print(str(player.player_id) + ": " + player.status.name + "----" + str(player.total()))
        print("------------------------------------------------------------------")


players = create_players(3)
play(players)
