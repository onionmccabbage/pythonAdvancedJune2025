import json
from weather import Weather

# NB get plenty of result brefore frciding on actual time
import timeit


def main(city='athlone'):
    fin = open(f'/data/{city}_weather.jreview4_weatherson', 'r')
    w = fin.read()
    w_dict = json.loads(w)
    desc = w_dict['weather'][0]['description']
    temp = w_dict['main']['temp']
    city = w_dict['name']
    # make a Weather instance
    w = Weather(city, desc, temp)
    print(w)

def checkCity(c):
    if c.lower() in ('athlone', 'athens', 'dublin', 'kista', 'madrid', 'turin'):
        return c
    else:
        return 'athlone'

if __name__ == '__main__':
    whichCity = input('Which city? ')
    start=timeit.default_timer()
    
    city = checkCity(whichCity)
    main(city)
    end=timeit.default_timer()

    print(f'Total time to retrieve weather reports {end-start}')