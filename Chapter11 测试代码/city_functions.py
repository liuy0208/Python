def get_city_country_relation(city,country,population=''):
    """说出一个城市及其所属国家。"""
    city = city.title()
    country = country.title()
    if population:
        city_country_relation = f"{city},{country} - population {population}"
    else:
        city_country_relation = f"{city},{country}"
    return city_country_relation