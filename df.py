# import requests
# from datetime import datetime

# def where_is_iss():
#     """Где сейчас МКС?"""
#     url = "http://api.open-notify.org/iss-now.json"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         position = data['iss_position']
#         timestamp = datetime.fromtimestamp(data['timestamp'])
        
#         print(f"""
# 🛰️ МКС сейчас находится:
#    🌍 Широта: {position['latitude']}
#    🌍 Долгота: {position['longitude']}
#    🕐 Время: {timestamp}
   
#    👉 Посмотреть на карте: 
#    https://www.google.com/maps/@{position['latitude']},{position['longitude']},4z
#         """)

# def astronauts():
#     """Кто сейчас в космосе?"""
#     url = "http://api.open-notify.org/astros.json"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         print(f"👨‍🚀 Сейчас в космосе {data['number']} человек:")
#         for person in data['people']:
#             print(f"   - {person['name']} на {person['craft']}")

# # Тестируем
# where_is_iss()
# astronauts()


import requests

def country_info(country="russia"):
    """Информация о стране"""
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()[0]
        name = data['name']['common']
        capital = data.get('capital', ['Нет'])[0]
        population = data['population']
        area = data['area']
        region = data['region']
        
        print(f"""
🌍 Информация о {name}:
   🏛️ Столица: {capital}
   👥 Население: {population:,} человек
   📏 Площадь: {area:,} км²
   🌎 Регион: {region}
   💰 Валюта: {list(data['currencies'].keys())[0]}
   🗣️ Языки: {', '.join(data['languages'].values())}
        """)

def random_country():
    """Случайная страна"""
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    
    if response.status_code == 200:
        import random
        countries = response.json()
        country = random.choice(countries)
        print(f"🎲 Случайная страна: {country['name']['common']}")

# Тестируем
country_info("japan")
country_info("brazil")
random_country()