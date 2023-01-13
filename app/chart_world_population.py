import utils 
import read_csv 
import charts 
import pandas as pd

def run():
    #world_population = read_csv.read_csv('./world_population.csv')
    df = pd.read_csv('world_population.csv')
    #world_population = list(filter(lambda item: item['Continent'] == 'South America', world_population))
    df = df[df['Continent'] == 'South America']
    #wp_percentage_dic = utils.new_dic(world_population, 'World Population Percentage')
    #print(wp_percentage_dic)
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    #charts.generate_pie_chart(wp_percentage_dic.keys(), wp_percentage_dic.values())
    charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()