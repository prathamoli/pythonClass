a = {
    "properties":{
        "profile":{
            'name':'Ram',
            'education':[
                {'college':'abc','year':2018},
                {'college':'xyz','year':2020}
            ]
        },
        'followers':100000,
        'following':100,
    }
}

properties = a.get('properties')
profile = properties.get('profile')
print(profile.get('name'))
print(properties.get('followers'))
print(properties.get('following'))

education = profile.get('education')

for uu in education:
    print(uu.get('college'))
    print(uu.get('year'))


oil_prices = [
    {
        'oil_type':'petrol',
        'prices':[
            {
                'year':2018,
                'price':100
            },
            {
                'year':2019,
                'price':150
            },
            {
                'year':2020,
                'price':200
            },
        ]
    },
    {
        'oil_type':'diesel',
        'prices':[
            {
                'year':2018,
                'price':100
            },
            {
                'year':2019,
                'price':150
            },
            {
                'year':2020,
                'price':200
            },
        ]
    }
]


print('----------------------------------')
for oil in oil_prices:
    print(f'oil type : {oil.get("oil_type").capitalize()}')
    total_price = 0
    for price in oil.get("prices"):
        print(f'year : {price.get("year")} : price :{price.get("price")}')
        total_price += price.get('price')
    average = total_price/3
    print(f'average : {average}')
    print('-----------------------------')
