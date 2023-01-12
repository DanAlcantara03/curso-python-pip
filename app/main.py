import utils

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    },
    {
        'Country': 'Mexico',
        'Population': 1200
    }
]

def run():
    keys, values = utils.get_popoulation()
    print(keys, values)

    country = input('Type Country => ').lower().capitalize()

    print(utils.population_by_country(data, country))

if __name__ == '__main__':
    run()