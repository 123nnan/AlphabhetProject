# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# monday = data[data.day == 'Monday']
# print(float((9 / 5 * monday.temp) + 32))
#
# # Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv('new_data.csv')

sd = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240429.csv")

grey_squirrel = sd[sd['Primary Fur Color'] == 'Gray']
black_squirrel = sd[sd['Primary Fur Color'] == 'Black']
red_squirrel = sd[sd['Primary Fur Color'] == 'Cinnamon']
grey_squirrel_count = len(sd[sd['Primary Fur Color'] == 'Gray'])
black_squirrel_count = len(sd[sd['Primary Fur Color'] == 'Black'])
red_squirrel_count = len(sd[sd['Primary Fur Color'] == 'Cinnamon'])

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(data_dic)
df.to_csv('squirrel_count.csv')