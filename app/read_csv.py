import csv
import re

def read_csv(path):
    data = []
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader)
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key,value in iterable}
            data.append(country_dict)

    return data


if __name__ == '__main__':
    data = read_csv('./world_population.csv') 
    print(data[0])
