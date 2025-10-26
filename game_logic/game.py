from utils.deck import shuffle, create_deck, compare_cards


def create_player(name: str = 'AI') -> dict:
    return {"name": name, "hand": [], "won_pile": []}


def init_game() -> dict:
    player1 = create_player(name='P1')
    player2 = create_player(name='P2')
    new_shuffled_deck = shuffle(create_deck())
    player1["hand"] = new_shuffled_deck[:26]
    player2["hand"] = new_shuffled_deck[26:]
    return {"deck": new_shuffled_deck, "player_1": player1, "player_2": player2}


def play_round(p1: dict, p2: dict):
    p1_card = p1["hand"].pop(0)
    p2_card = p2["hand"].pop(0)
    winner = compare_cards(p1_card, p2_card)

    print(f'{p1["name"]} card:{p1_card["value"]} vs {p2["name"]} card:{p2_card["value"]}', end=" =\t")

    match winner:
        case 'p1':
            print(f'{p1["name"]} wins!', end=" ")
            p1["won_pile"].append(p1_card)
            p1["won_pile"].append(p2_card)
            print(f'{p1["name"]} has {len(p1["won_pile"])} victory cards')
        case 'p2':
            print(f'{p2["name"]} wins!', end=" ")
            p2["won_pile"].append(p1_card)
            p2["won_pile"].append(p2_card)
            print(f'{p2["name"]} has {len(p2["won_pile"])} victory cards')
        case 'WAR':
            print(f"WAR:{p1_card['value']} vs {p2_card['value']}")
            war(p1, p2)
        case _:
            print("error")


def war(p1: dict, p2: dict):
    p1_cards = []
    p2_cards = []
    while len(p1["hand"]) >= 4 and len(p2["hand"]) >= 4:
        p1_cards += [p1["hand"].pop(0) for _ in range(4)]
        p2_cards += [p2["hand"].pop(0) for _ in range(4)]

        print(
            f"{p1['name']}'s fourth card:{p1_cards[-1]['value']} vs {p2['name']}'s fourth card:{p2_cards[-1]["value"]}",
            end=" = ")

        winner = compare_cards(p1_cards[-1], p2_cards[-1])

        match winner:
            case 'p1':
                print(f"{p1["name"]} wins!")
                p1["won_pile"] += p1_cards
                p1["won_pile"] += p2_cards[:]
                break
            case 'p2':
                print(f"{p2["name"]} wins!")
                p2["won_pile"] += p1_cards
                p2["won_pile"] += p2_cards
                break
            case 'WAR':
                print(f"WAR:{p1_cards[-1]} vs {p2_cards[-1]}")
            case _:
                print("error")
                break
