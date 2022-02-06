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
    'cookie': 'first_time_visit=rOfaWQRIkgbxQyF%2FDh%2BF%2FUccrC7SW%2BLOOJO7UQb2cbBK0%2BCPNDWAyV5z4T0iuBirfHes7s%2Fy8lNkGiUkj6tkWbffrRLLywo%2Bzg%3D%3D--EGSIGE4IUZMhwodC--SP2EosF28DIF12yu%2B9upTg%3D%3D; _gcl_au=1.1.1316643649.1643803125; _ga=GA1.2.1674399226.1643803125; _fbp=fb.1.1643803125645.1672580157; _pin_unauth=dWlkPU5UUmxNVEl3TVRRdFpqQTFNUzAwTmpZNExUZ3haV0l0WlRjeU5tVmpPR1JqT0dSaQ; _hjSessionUser_1506979=eyJpZCI6IjA2MzQ2ODlkLWU5MTMtNTdhOS1iM2MzLTgzZjllMGZkMjg3MSIsImNyZWF0ZWQiOjE2NDM4MDMxMjU2NzEsImV4aXN0aW5nIjp0cnVlfQ==; client_cache_key=LUUC4NV%2FGCJibd%2B8UQtTQ1rQNpmmNYJUQa0zqtGCUg4aXjRguhhXAr%2BIEsP7UN18CzcfLWsOPNc1SlaFmG4LW1OREdDt%2BT2mUplEXxlVgzgSxopx6firL2ESHH%2Fc5yINwYE1dDqrRM0t--IirL%2FO1JnbKu0yU4--4shvlMB8Xec7xZRgJEOC%2BQ%3D%3D; eeny_meeny_personalized_upsell_module_v2=XvhavvlGR9a4EzBmDsJE34krraTlOUWnV9FRCYykp9BlcHrLUh5k3B0hSKmOt%2BZqSrrsgqwrTGtMeHl%2BIteuFw%3D%3D; eeny_meeny_personalized_cross_sell_v2=KZW1u1DVp85reY5Bu%2FA2mYA9PBbqDeB5vo6R3aiZ%2Bh7UaQy%2F1j3HvF5tg%2F0Evh7r2W2JREUltkm0NhYCVp7Q5g%3D%3D; eeny_meeny_supercards_offers_page_v2=BDXk0U590RNlRKNE0297rGLaHnkAEt44sIAwuUhnFPn0O1Ctr%2Bmv2%2Fmg2JylzaxrWN%2BVzA1%2FJlqq7RLvPNDOSQ%3D%3D; eeny_meeny_pam_merchant_links_v1=aNZ%2BTOx%2BbPgJGNFMWiQ94sQAmy2xaXRVW7VZW2jC2HKHhetmq6jYR0tszsfnqsNRVrV2KJcvQSN0qa%2Ba7NVpB7ILH5noHRmEEngxw4P%2BDS8%3D; _hjSession_1506979=eyJpZCI6IjkzZTRhYjUyLTMyNmUtNGZiNC1hZWVkLTUzNTk1OWMyZmZjYSIsImNyZWF0ZWQiOjE2NDQwNTgwNDMzNDgsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _gid=GA1.2.1903282352.1644058043; _clck=1snx8w3|1|eyq|0; _hjIncludedInSessionSample=1; _hp2_ses_props.3503103446=%7B%22r%22%3A%22https%3A%2F%2Fwww.vivino.com%2F%22%2C%22ts%22%3A1644061466333%2C%22d%22%3A%22www.vivino.com%22%2C%22h%22%3A%22%2Fexplore%22%2C%22q%22%3A%22%3Fe%3DeJzLLbI10TNSy83MszVQy02ssDU1AAG15Epb7yC1ZCARrlZga6iWnmZblliUmVqSmKOWX5Riq5afVGkLACo3Es0%253D%22%7D; recently_viewed=XpqZEa9rEm6VQhSC%2BfqbscASuj3tIzS11l9WCU9%2BpygP7zoi%2FwBjDj3AnF6hSp1S%2By8HEQPsnecBJRUsaMgB3enhITbK0VyCB3iCUW6UGRL7unzF6DwfD3hhiXCQ2Y9WALDb8Q7KBreNpurKirRGIugxwWI7p%2FBmV8pkzcDg%2B5RXAtR9vYCpECPtf63Wwgj8zh1%2BWQbNYUK9s7JDkpl%2B2XidyWjex5EKMZMTveKaVQIGwD2XSVB%2FgsKnS8ZBwj3xKsoeu%2FcmUxjJ%2FuWXTWFjzbR50IvxJuZIHY%2BkMfH5NEmccH8ldAWR6%2Fpqdnt7kjALJIX5bjGms0ONNF5kB1JptJe3XBbd52subWN%2FKnuhp9yLgpdD%2BZuRQzrBksLCv7%2FzYP9OTaFycK%2Bo%2BdKlbSOGWadbuM%2BlCMFJKJeplizqVUzbjqUt0Ky%2B3YUjo8WrXEj2J0n3kvpNY3lpqjVsVM5fdo0%3D--n%2B%2F3khVHVkYIltBZ--A2GFMcmiyOgd0YXVJkrGCg%3D%3D; _hp2_id.3503103446=%7B%22userId%22%3A%221031566393289373%22%2C%22pageviewId%22%3A%224940871595221018%22%2C%22sessionId%22%3A%228499131893530182%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _gat_UA-222490-2=1; _uetsid=00245630867111ecbcc413580addbee1; _uetvid=798cf2b0841f11ecb4250dc486dbee8f; merchandizing_split_tests=kFDkhIzNu6MicUQrEsfGpqYBDMX9%2FPDPpYuhAqEjrVK6jWGciwxU9Hamk%2FGcCvTMS4xPh5Tt6On9B7tzycdvCHQy0twvsf%2FMh67%2FN3A%3D--NtmnMPXVBoX7UMxY--iYdZV24g%2FY1V6IzslT%2BsRA%3D%3D; cto_bundle=Hox7C19iJTJCaUhMV2Fpa2w5YWd5OXlnUlZxZUFRJTJGTiUyRiUyRmwzUmc3RUFCQmVOMGU5SDlZOSUyQnltS2NCNmRnQTY4ZGlqQjhBWEhrdE9pcDFqNVhmQ1hDTGRYeU1MV3RDbzlLcW51d1IlMkZzJTJCeWFRenFXa0hlOE1XZmJpSUZHUTd3cno2QWM0dk9rN0FhdEhDUTVaSHZ0TzFzZEw2cmVYZyUzRCUzRA; _clsk=18a07eg|1644062470777|24|0|a.clarity.ms/collect; _ruby-web_session=g7lzrGLMXLnWL%2BzIzUe5ZUZ4z5cQbYT%2FTC6ffesYK7zWYcmlWaFOft9EGbAs%2F1Gyxwl%2BvIgzeRdnun%2BfX%2BeSac46GlH2VgHtQDtXjibymntCQg3uqW396fVM93LzbrSVFhc4elbrkeeFbAls709XCuHxRtHz%2FkR9gwy3xRfQM5IBdyFweUfc%2BQAvFcVjcfFbbQR9Dlrv6wJOThSfE%2FDhg0FG992hlIt%2F2YLz4e4qcD%2FzpL4jcMHUFw3He30YUqvHF3BfsIiDSZmkQKDKGHPfYIpwmEGJyzITzOImu%2FZaFXlwsUMs0nCSso%2BJAB1PRiSLf7eaCoxBF5ZCYZtHlpyrgo1%2FeKPlmaKGIVDLlJQLC%2BWfxUxvUfZtI9j1LFQbQEO6VjW1C5C27erD4mUdzK5f3cEnysppDFUJQsNccqTXt2IuWw%2BXTBexAG1Y8l78f%2FFUcDVVQxAKFFsQnGw4h3Iu5qy8Nuy0mAveOiswl8biQBAtcmVbgw%3D%3D--irFu01Tgt2gPbQKJ--Ej%2BPDeujOyX3Cw%2B91Vkc2g%3D%3D'
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
                    'cookie': 'first_time_visit=rOfaWQRIkgbxQyF%2FDh%2BF%2FUccrC7SW%2BLOOJO7UQb2cbBK0%2BCPNDWAyV5z4T0iuBirfHes7s%2Fy8lNkGiUkj6tkWbffrRLLywo%2Bzg%3D%3D--EGSIGE4IUZMhwodC--SP2EosF28DIF12yu%2B9upTg%3D%3D; _gcl_au=1.1.1316643649.1643803125; _ga=GA1.2.1674399226.1643803125; _fbp=fb.1.1643803125645.1672580157; _pin_unauth=dWlkPU5UUmxNVEl3TVRRdFpqQTFNUzAwTmpZNExUZ3haV0l0WlRjeU5tVmpPR1JqT0dSaQ; _hjSessionUser_1506979=eyJpZCI6IjA2MzQ2ODlkLWU5MTMtNTdhOS1iM2MzLTgzZjllMGZkMjg3MSIsImNyZWF0ZWQiOjE2NDM4MDMxMjU2NzEsImV4aXN0aW5nIjp0cnVlfQ==; client_cache_key=LUUC4NV%2FGCJibd%2B8UQtTQ1rQNpmmNYJUQa0zqtGCUg4aXjRguhhXAr%2BIEsP7UN18CzcfLWsOPNc1SlaFmG4LW1OREdDt%2BT2mUplEXxlVgzgSxopx6firL2ESHH%2Fc5yINwYE1dDqrRM0t--IirL%2FO1JnbKu0yU4--4shvlMB8Xec7xZRgJEOC%2BQ%3D%3D; eeny_meeny_personalized_upsell_module_v2=XvhavvlGR9a4EzBmDsJE34krraTlOUWnV9FRCYykp9BlcHrLUh5k3B0hSKmOt%2BZqSrrsgqwrTGtMeHl%2BIteuFw%3D%3D; eeny_meeny_personalized_cross_sell_v2=KZW1u1DVp85reY5Bu%2FA2mYA9PBbqDeB5vo6R3aiZ%2Bh7UaQy%2F1j3HvF5tg%2F0Evh7r2W2JREUltkm0NhYCVp7Q5g%3D%3D; eeny_meeny_supercards_offers_page_v2=BDXk0U590RNlRKNE0297rGLaHnkAEt44sIAwuUhnFPn0O1Ctr%2Bmv2%2Fmg2JylzaxrWN%2BVzA1%2FJlqq7RLvPNDOSQ%3D%3D; eeny_meeny_pam_merchant_links_v1=aNZ%2BTOx%2BbPgJGNFMWiQ94sQAmy2xaXRVW7VZW2jC2HKHhetmq6jYR0tszsfnqsNRVrV2KJcvQSN0qa%2Ba7NVpB7ILH5noHRmEEngxw4P%2BDS8%3D; _hjSession_1506979=eyJpZCI6IjkzZTRhYjUyLTMyNmUtNGZiNC1hZWVkLTUzNTk1OWMyZmZjYSIsImNyZWF0ZWQiOjE2NDQwNTgwNDMzNDgsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _gid=GA1.2.1903282352.1644058043; _clck=1snx8w3|1|eyq|0; _hjIncludedInSessionSample=1; _hp2_ses_props.3503103446=%7B%22r%22%3A%22https%3A%2F%2Fwww.vivino.com%2Fexplore%3Fe%3DeJzLLbI10TNSy83MszVQy02ssDU1AAG15Epb7yC1ZCARrlZga6iWnmZblliUmVqSmKOWX5Riq5afVGkLACo3Es0%253D%22%2C%22ts%22%3A1644063998244%2C%22d%22%3A%22www.vivino.com%22%2C%22h%22%3A%22%2Ffr-chateau-latour-grand-vin-pauillac-premier-grand-cru-classe%2Fw%2F1655970%22%2C%22q%22%3A%22%3Fyear%3D2003%26price_id%3D4067491%22%7D; recently_viewed=BrdYydOSj3lch0VyfrUbJ9G5cSofR1AolM8plB2sQJiv4LUPpC6HKD8x8fJ%2BezEDf7w%2Fu%2FDDMjw%2FdkMptAhctV6O2%2BOn8IZrQMZQnLCV3IAGa%2BTj9UjY0aq63gCUHFkBivsBoLR6goSKXz8u8zH5Pvd5ZFOGXGWvbxQNKSsycPawBj8OZKgSuuCf%2BXH%2Foiz4DZ3Ucmpk33gWS1BSLjnGGQCa30K8Dj5N2ivHQr1OrG1xqpy0dSIRgCEmUisF3RicD1CJYN5mWvktOiYcq5PE%2BkrwiYSLrp7ZSZrT1Ze5ZMQwh3nN%2BxkdzCk2GaIDL2%2BBvkJaWTi6WBfrIJpbT7MpFvIExlqbOPglZ1y8jI04vVWBOVrCXK5ia0Fa8kqCdbgWG4CVHRV%2Fdw4%2F%2F3zlObZ8VO7frRZHq%2BtlWz%2BSocsgKZs5743oEpqz6MrIiCow%2Bdl1e0%2F2nAn5x4NefBtwvIYLMdVO8DCv--lTl53lFFbOZm5KUq--TVjkJrGMJrw6TCSPsUvOcg%3D%3D; _gat_UA-222490-2=1; _uetsid=00245630867111ecbcc413580addbee1; _uetvid=798cf2b0841f11ecb4250dc486dbee8f; _hp2_id.3503103446=%7B%22userId%22%3A%221031566393289373%22%2C%22pageviewId%22%3A%226219300431999167%22%2C%22sessionId%22%3A%221666912969205532%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; cto_bundle=MpLQH19iJTJCaUhMV2Fpa2w5YWd5OXlnUlZxZUFXRkhoa1c3QUtsMWxwSGlpOWNUQlAlMkZrT2d0eWswWmpXVGhoMGVyR3llMHRyVFoxaHJsbEw2dnlzRSUyRmRuWHNUWWx2ZzNQUmhOSUtUY2wzeHl5JTJCdkJ2eFdKT0VRSlFYc1RZMyUyRjRoc2pTa3VxZkxOS1d5czV3eERKa0R5YkZlaExRJTNEJTNE; merchandizing_split_tests=RgMzAOjCqq0FqPmauu5RYWJ7i%2FnailZgOTAbRwZ6EyF9qORa5K8UBjkKXrFpsphPwQ2iRXUG%2F8zWI7Ipojx%2BcfpdNKiZAFrR0rUhpOg%3D--%2FZ%2BL%2B5qHcCVNTTzF--WfsqKU%2Bw8XmUYeLkH%2B924Q%3D%3D; _clsk=18a07eg|1644065202839|44|0|a.clarity.ms/collect; _ruby-web_session=9ugV2dQzDWft95UdkykNaHT1A8kmch%2BgrAc7kfv7YP8xjhRGj1fIgQc1zl%2BpBv2qT%2Fh21k7gAI%2BmHJfLFfb1joKol%2BfYf6fzhGwjupdiQ0%2B6AQt2oZAQr43nxOC3N%2Bp4LBZCWbk2%2FfcVbyFPn4Okdu6YIeA5lb2klxhR%2BJKu%2FHLa4t%2BxkhLBHuc22s0xW5N8Ul4%2Fsa6IQfLQPHkKphWECqv9L6UkAU4W5%2FbgFkUsa8%2B9Hx8MQf7oTeSbtqLcdSYNqGv01z05rsX%2FZOBNm2v4%2F362AqqvLKkRLKXzPSKVFl2y8SpVQuH5wSz2rzYKSueduDs6aEya0fo6RenooBeAE1weTqEWWGNQQpEMuLIhBg3UGZPe68jFQubpX9S2K2xXEkoNINBCNTrO9R9%2FsrhKm%2FDVXp%2FEn5bViX6%2BIYMr2Uhs%2F4FXL7DFnxbv%2BEI4s5dmNb3ZL6t0GIY5%2BHRzGswOWjTy12wjBBE%2F%2FkDb%2BCNxQlDij%2BvU9Q%3D%3D--SzA8Kh4nQ1DB1ljk--MTTy8QyIJWDZdF94H3hJQQ%3D%3D'
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
