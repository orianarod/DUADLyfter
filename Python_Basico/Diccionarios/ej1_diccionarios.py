hotel = { 
    'name' : 'Motel9',
    'stars' : 1,
    'rooms' : [ 
        {'number': 1, 'floor' : 1, 'price_per_night' : 20},
        {'number': 2, 'floor' : 1, 'price_per_night' : 20},
        {'number': 3, 'floor' : 1, 'price_per_night' : 20},
        {'number': 4, 'floor' : 2, 'price_per_night' : 25},
        {'number': 8, 'floor' : 2, 'price_per_night' : 25},
        {'number': 5, 'floor' : 2, 'price_per_night' : 25}
    ]
}

for field, data in hotel.items():
    print(f'{field}: {data}')


