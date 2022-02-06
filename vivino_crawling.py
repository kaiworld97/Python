import requests
import json
import time
import os
import csv

headers = {
    'authority': 'www.vivino.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'x-requested-with': 'XMLHttpRequest',
    'scheme': 'https',
    'charset': 'utf-8',
    'accept-encoding': 'gzip, deflate, br',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': ''
}
# response = requests.get(f'https://www.vivino.com/api/explore/explore?country_code=KR&currency_code=KRW&grape_filter=varietal&min_rating=4.2&order_by=&order=&price_range_max=500000&price_range_min=0&page=1&language=en', headers=headers)
#
# print(response.json()['explore_vintage']['matches'][0]['price']['amount'])
# print(response.json()['explore_vintage']['matches'][0]['vintage']['wine']['id'])
# print(response.json()['explore_vintage']['matches'][0]['vintage']['name'])
# print(response.json()['explore_vintage']['matches'][0]['vintage']['year'])
# print(response.json()['explore_vintage']['matches'][0]['vintage']['wine']['region']['country']['name'])
# print(response.json()['explore_vintage']['matches'][0]['vintage']['wine']['region']['name'])
# print(response.json()['explore_vintage']['matches'][0]['vintage']['image']['variations']['bottle_large'])

# 1 ~ 81

wine_list = []
try:
    for num in range(1, 81):
        response = requests.get(
            f'https://www.vivino.com/api/explore/explore?country_code=KR&currency_code=KRW&grape_filter=varietal&min_rating=4.2&order_by=&order=&price_range_max=500000&price_range_min=0&page={num}&language=en',
            headers=headers)
        for i in response.json()['explore_vintage']['matches']:
            wine = []
            wine_id = i['vintage']['wine']['id']
            wine.append(wine_id)
            if i['vintage']['wine']['type_id'] == 1:
                wine.append('red')
            elif i['vintage']['wine']['type_id'] == 2:
                wine.append('White')
            elif i['vintage']['wine']['type_id'] == 3:
                wine.append('Sparkling')
            elif i['vintage']['wine']['type_id'] == 4:
                wine.append('Rosé')
            elif i['vintage']['wine']['type_id'] == 7:
                wine.append('Dessert')
            elif i['vintage']['wine']['type_id'] == 24:
                wine.append('Fortified')
            wine.append(i['vintage']['statistics']['ratings_average'])
            wine.append(i['vintage']['name'])
            wine.append(i['vintage']['seo_name'])
            wine.append(i['vintage']['wine']['winery']['name'])
            wine.append(i['vintage']['wine']['name'])
            wine.append(i['vintage']['year'])
            wine.append(i['vintage']['wine']['region']['country']['name'])
            wine.append(i['vintage']['wine']['region']['name'])
            time.sleep(2)
            try:
                headers1 = {
                    'authority': 'www.vivino.com',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'x-requested-with': 'XMLHttpRequest',
                    'scheme': 'https',
                    'accept-encoding': 'gzip, deflate, br',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                    'content-type': 'application/json',
                    'accept': 'application/json',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie': ''
                }
                response1 = requests.get(
                    f'https://www.vivino.com/api/wines/{wine_id}/tastes?language=en',
                    headers=headers1)
                flavor = []
                for j in response1.json()['tastes']['flavor']:
                    flavor.append(j['group'])
                wine.append(flavor)
                if response1.json()['tastes']['structure']['acidity'] is None:
                    wine.append(0)
                else:
                    wine.append(response1.json()['tastes']['structure']['acidity'])
                if response1.json()['tastes']['structure']['intensity'] is None:
                    wine.append(0)
                else:
                    wine.append(response1.json()['tastes']['structure']['intensity'])
                if response1.json()['tastes']['structure']['sweetness'] is None:
                    wine.append(0)
                else:
                    wine.append(response1.json()['tastes']['structure']['sweetness'])
                if response1.json()['tastes']['structure']['tannin'] is None:
                    wine.append(0)
                else:
                    wine.append(response1.json()['tastes']['structure']['tannin'])
            except:
                continue
            wine.append(i['price']['url'])
            wine.append(i['price']['amount'])
            wine.append(i['vintage']['image']['variations']['bottle_large'])
            wine.append(i['vintage']['image']['variations']['bottle_medium'])
            wine.append(i['vintage']['image']['variations']['bottle_small'])

            print(wine)
            wine_list.append(wine)
            time.sleep(3)
        time.sleep(5)
except:
    pass
completeName = os.path.join("wine1922.csv")
file = open(completeName, mode="w", encoding='utf-8')
writer = csv.writer(file)
for i in wine_list:
    # print(i)
    writer.writerow(i)
# writer.writerow([response.json()['explore_vintage']['matches']])
