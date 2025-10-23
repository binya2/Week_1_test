from utils.deck import shuffle, create_deck


def create_player(name:str = 'AI') -> dict:
    return {"name":name, "hand":[], "won_pile":[]}


def init_game()->dict:
    player1 = create_player(name='P1')
    player2 = create_player(name='P2')
    new_shuffl_deck =  shuffle(create_deck())
    player1["hand"] = new_shuffl_deck[:26]
    player2["hand"] = new_shuffl_deck[26:]

    return {"deck": new_shuffl_deck, "player_1": player1, "player_2": player2}

