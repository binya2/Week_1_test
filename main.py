from game_logic.game import init_game, play_round


def run():
    players_dict: dict = init_game()
    player_1 = players_dict["player_1"]
    player_2 = players_dict["player_2"]
    while player_1["hand"] != [] and player_2["hand"] != []:
        play_round(players_dict["player_1"], players_dict["player_2"])
    winner = {}
    if len(player_1["won_pile"]) > len(player_2["won_pile"]):
        winner = player_1

    if len(player_1["won_pile"]) < len(player_2["won_pile"]):
        winner = player_2

    if winner != {}:
        print(f"{winner['name']} wins! With {len(winner['won_pile'])} cards")
    else:
        print("Draw - Both win")


if __name__ == "__main__":
    run()
