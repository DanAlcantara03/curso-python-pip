import re
import utils
import read_csv as rcsv
import charts as chrt

# get_cute_format_list_
def gcfl(list, simb):
    cute_format_list = ''
    for element in list:
        cute_format_list += ('\n' + (' ' * 2) + simb + '  ' + element) 
    return cute_format_list


def dicc_sc(word_population, country):
    for dic in word_population:
        if dic.get('Country/Territory') != country:
            continue    
        return dic


def reduce_dictionary(dict):
    return {key[0:4]: int(value) for key, value in dict.items() if re.findall('[0-9]+', key[0:4]) and 'Population' in key}


def run():
    word_population = rcsv.read_csv('./world_population.csv')
    countries = utils.get_list_of_something(word_population, 'Country/Territory')#get_list_of_countries(word_population)
    selectioned_country = input("\nAvailable countries for charting: \n" + gcfl(countries, '\u272A') + "\n\nPlease select a country: ").title()

    while selectioned_country not in countries:
        selectioned_country = input("\n\nPlease select a valid country: ").title()

    dic_selected_country = dicc_sc(word_population, selectioned_country)
    #print(dic_selected_country)
    dic_selected_country = reduce_dictionary(dic_selected_country)
    #print(dic_selected_country)
    chrt.generate_bar_chart(dic_selected_country.keys(), dic_selected_country.values(), selectioned_country)


if __name__ == '__main__':
    run()