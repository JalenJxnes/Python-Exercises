import requests
import pandas as pd

print("Environment configured...")
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
csv = "nba.csv"

response = requests.get(url)
response.raise_for_status() #checks if request was successful
with open(csv, "wb") as f:
  f.write(response.content)

print("Download Complete...")

df = pd.read_csv("nba.csv")
print("DataFrame Ready!")

#Solution 1
print("\n\n\nTotal Points by NBA Franchise")
print(df["team_id"].value_counts())

#Solution 2
print("\n\n\nFinal Game Results for Games 5555 through 5559")
print(df.loc[5555:5559, ["fran_id", "opp_fran", "pts", "opp_pts"]])

#Solution 3
print("\n\n\n2015 Warrior W/L Stats:")
print(df[(df["fran_id"] == "Warriors") & (df["year_id"] == 2015)].groupby(["game_result"])
["game_id"].count())