import csv

with open('files/weather.csv', 'r') as file:
    data = list(csv.reader(file))

city = input('Enter a city: ')

for row in data[1:]:
    if row[0] == city:
        print(row[1])


# csv module allows me to read csv files and store them in lists for example, then I can extract any kind of information