# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

nobel = pd.read_csv("data/nobel.csv")

top_gender = nobel["sex"].value_counts().idxmax()
top_country = nobel["birth_country"].value_counts().idxmax()


nobel["usa_born_winner"] = nobel["birth_country"] == "United States of America"
nobel["decade"] = (nobel["year"] // 10) * 10

usa_ratio = nobel.groupby("decade")["usa_born_winner"].mean()
max_decade_usa = int(usa_ratio.idxmax())


nobel["female_winner"] = nobel["sex"] == "Female"

female_ratio = (
    nobel.groupby(["decade", "category"])["female_winner"]
    .mean()
    .reset_index()
)

max_row = female_ratio.loc[female_ratio["female_winner"].idxmax()]
max_female_dict = {
    int(max_row["decade"]): max_row["category"]
}

first_woman = (
    nobel[nobel["sex"] == "Female"]
    .sort_values("year")
    .iloc[0]

)

first_woman_name = first_woman["full_name"]
first_woman_category = first_woman["category"]


repeat_list = (
    nobel["full_name"]
    .value_counts()
    .loc[lambda x: x > 1]
    .index
    .tolist()
)