import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"].tolist()

red = []
black = []
grey = []

for color in fur_color:
    if color == "Gray":
        grey.append(color)
    elif color == "Black":
        black.append(color)
    elif color ==  "Cinnamon":
        red.append(color)

color_counts = {
    "Color": ["Red", "Black", "Grey"],
    "Count": [len(red), len(black), len(grey)]
}

color_df = pandas.DataFrame(color_counts)

color_df.to_csv("squirrel_color_counts.csv")