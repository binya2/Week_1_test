import random


def create_card(rank: str, suite: str) -> dict:
    rank_dict = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                 'K': 13}
    return {"rank": rank, "suite": suite, "value": rank_dict[rank]}


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card['value'] > p2_card['value']:
        return "p1"
    elif p1_card['value'] < p2_card['value']:
        return "p2"
    else:
        return "WAR"


def create_deck() -> list[dict]:
    suite_dict = {0: 'H', 1: 'C', 2: 'D', 3: 'S'}
    rank_revers_dict = {0: 'A', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7',
                        7: '8', 8: '9', 9: '10', 10: 'J', 11: 'Q', 12: 'K'}
    deck_cards: list[dict] = []
    for i in range(52):
        num = i % 13
        side = int(i / 13)
        deck_cards.append(create_card(rank_revers_dict[num], suite_dict[side]))
    return deck_cards


def shuffle(deck: list[dict]) -> list[dict]:
    shuffle_list = deck.copy()
    for i in range(1000):
        num1 = random.randrange(1, 52)
        num2 = random.randrange(1, 52)
        if num1 == num2:
            i -= 1
            continue
        shuffle_list[num1], shuffle_list[num2] = shuffle_list[num2], shuffle_list[num1]

    return shuffle_list
