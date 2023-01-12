import utils 
import read_csv 
import charts 


def run():
    world_population = read_csv.read_csv('./world_population.csv')
    world_population = list(filter(lambda item: item['Continent'] == 'South America', world_population))
    wp_percentage_dic = utils.new_dic(world_population, 'World Population Percentage')
    #print(wp_percentage_dic)
    charts.generate_pie_chart(wp_percentage_dic.keys(), wp_percentage_dic.values())

if __name__ == '__main__':
    run()