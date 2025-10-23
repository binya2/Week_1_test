from utils.deck import shuffle, create_deck, compare_cards


def create_player(name:str = 'AI') -> dict:
    return {"name":name, "hand":[], "won_pile":[]}


def init_game()->dict:
    player1 = create_player(name='P1')
    player2 = create_player(name='P2')
    new_shuffl_deck =  shuffle(create_deck())
    player1["hand"] = new_shuffl_deck[:26]
    player2["hand"] = new_shuffl_deck[26:]

    return {"deck": new_shuffl_deck, "player_1": player1, "player_2": player2}


def play_round(p1:dict,p2:dict):
    p1_card = p1["hand"].pop(0)
    p2_card = p2["hand"].pop(0)
    winer = compare_cards(p1_card, p2_card)
    print(f"{p1["name"]} card: {p1_card['value']} vs {p2["name"]} card: {p2_card['value']}", end= "=\t" )

    match winer:
        case 'p1':
            print(f"{p1["name"]} wins!")
            p1["won_pile"].append(p1_card)
            p1["won_pile"].append(p2_card)
        case 'p2':
            print(f"{p2["name"]} wins!")
            p2["won_pile"].append(p1_card)
            p2["won_pile"].append(p2_card)
        case 'WAR':
            print(f"WAR:{p1_card['value']} vs {p2_card['value']}")
            p1["won_pile"].append(p1_card)
            p2["won_pile"].append(p2_card)
        case _:
            print("error")
