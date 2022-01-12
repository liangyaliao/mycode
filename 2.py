#!/usr/bin/env python3
import pandas as pd
header_list= ["GameId", "GameDate", "OffenseTeam", "DefenseTeam"]
df = pd.read_csv('nfl2020.txt', index_col="GameId")
i = int(input("Please enter the GameId: "))
games_df= df.loc[i]

games_df.drop(games_df.columns.difference(header_list), 1, inplace=True)
print(games_df.head(10))
