import pandas as pd

url = 'https://en.wikipedia.org/wiki/World_Surf_League#Surfers_with_the_most_World_Tour_wins_(Men)'
df = pd.read_html(url)

print(len(df))
steps = df[3]

print(steps[['Position','Name','Steps Won']])


'''

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df)
'''
