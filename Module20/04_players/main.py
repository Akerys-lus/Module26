players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_players_tuple = list(i_key + i_value for i_key, i_value in players.items())
print(new_players_tuple)
