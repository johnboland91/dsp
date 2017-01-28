import pandas as pd

url = "https://raw.githubusercontent.com/johnboland91/dsp/master/python/football.csv"
data = pd.read_csv(url)
data["Net Goals"] = data["Goals"] - data["Goals Allowed"]
data["Net Goals Difference"] = abs(data["Net Goals"])
min_diff = min(data["Net Goals Difference"])
min_diff_index = data.loc[data['Net Goals Difference'].idxmin()]
print(min_diff_index["Team"])


