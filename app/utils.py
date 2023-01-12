def get_popoulation():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values

def population_by_country(data, country):    
    return list(filter(lambda item: item['Country'] == country, data))

def get_list_of_something(list_of_dict, an_specific_key):
    #for dic in word_population:
    #    countries.append(dic.get('Country/Territory'))
    return [dic.get(an_specific_key) for dic in list_of_dict]

def new_dic(list_of_dict, an_specific_key):
    #print(list_of_dict)
    return{dic.get('Country/Territory'): float(dic.get(an_specific_key)) for dic in list_of_dict}