import pandas

data = pandas.read_csv("weather_data.csv")

monday = data[data.day == "Monday"]

convert = int(monday["temp"].values[0])

F = (convert * 9) / 5 + 32
print(F)