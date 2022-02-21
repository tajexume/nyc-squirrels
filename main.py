import pandas
squirrels = {}
tot_cinnamon = 0
tot_grey = 0
tot_black = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
for squirrel in data["Primary Fur Color"].to_list():
  if squirrel == "Cinnamon":
    tot_cinnamon += 1
  elif squirrel == "Black":
    tot_black += 1
  elif squirrel == "Gray":
    tot_grey += 1
squirrels = {"Fur Color": ['Grey', 'Cinnamon', 'Black'], 'Count': [tot_grey, tot_cinnamon, tot_black]}
squir_data = pandas.DataFrame(squirrels)
squir_data.to_csv("Squirrel_Data.csv")
print(f"{squir_data}")