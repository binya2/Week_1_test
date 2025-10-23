
def create_card(rank:str,suite:str) -> dict:
    rank_dict = {'A':14, '2':2, '3':3, '4':4, '5':5,'6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
    return {"rank":rank, "suite":suite, "value":rank_dict[rank]}


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card['value'] > p2_card['value']:
        return "p1"
    elif p1_card['value'] < p2_card['value']:
        return "p2"
    else:
        return "WAR"