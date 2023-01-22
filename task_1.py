geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def geo_filter(geo_data, filter_name):
    geo_data_copy = geo_data.copy()
    for visit in geo_data:
        if filter_name not in list(visit.values())[0][1]:
            geo_data_copy.remove(visit)
    return geo_data_copy


# def geo_filter(geo_data, filter_name):
#     return list(filter(lambda x: list(x.values())[0][1] == filter_name, geo_data))


if __name__ == '__main__':
    country = 'Россия'
    print(geo_filter(geo_logs, country))
