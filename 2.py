#!/usr/bin/env python3

"""it is done with Chad's wisdom.If you enter the GameId, you will see the top 10's Gamedate, offense team and defense team. """

import pandas as pd
header_list= ["GameId", "GameDate", "OffenseTeam", "DefenseTeam"]
df = pd.read_csv('nfl2020.txt', index_col="GameId")
i = int(input("Please enter the GameId: "))
games_df= df.loc[i]

games_df.drop(games_df.columns.difference(header_list), 1, inplace=True)
print(games_df.head(10))
