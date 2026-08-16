import pandas as pd
print("Baseball Data Analytics")

data = {
    "Player": ["Jackson", "Martinez", "Williams", "Carter", "Davis"],
    "At_Bats":[200, 220, 190, 210, 205],
    "Hits": [58, 66, 51, 63, 55],
    "Home Runs": [14, 9, 17, 6, 12],
    "Strikeouts": [61, 35, 72, 28, 48],
    "Walks": [18, 30, 20, 35, 24],
    "Doubles": [12, 18, 11, 20, 15],
    "Triples": [2, 1, 3, 2, 1],
}

df = pd.DataFrame(data)
print(df)
df["Batting Average"] = df["Hits"] / df["At_Bats"]
print(df)
print(df.sort_values("Batting Average", ascending=False))
df["Strikeout_Rate"] = df["Strikeouts"] / df["At_Bats"]
print(df)
df["OBP"] = (df["Hits"] + df["Walks"]) / (df["At_Bats"] + df["Walks"])
print(df[["Player", "Batting Average", "OBP"]])
df["Singles"] = df["Hits"] - df["Doubles"] - df["Triples"] - df["Home Runs"]
df["Total Bases"] = df["Singles"] + (2 * df["Doubles"]) + (3 * df["Triples"]) + (4 * df["Home Runs"])
df["SLG"] = df["Total Bases"] / df["At_Bats"]
print(df[["Player", "Batting Average", "OBP", "SLG", "Home Runs"]])
df["OPS"] = df["OBP"] + df["SLG"]
print(df.sort_values("OPS", ascending=False))