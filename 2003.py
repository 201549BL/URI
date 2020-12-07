
def calc_delay(time):
    max_travel_time = 60
    a,b = [int(x) for x in time.split(':')]
    minutes = (a * 60) + b + max_travel_time
    hour = minutes // 60
    rest = minutes % 60
    
    if hour < 8:
        print('Atraso maximo: 0')
    elif hour == 8:
        print(f'Atraso maximo: {rest}')
    elif hour > 8:
        print(f'Atraso maximo: {((hour - 8) * 60) + rest}')


calc_delay('5:00')

