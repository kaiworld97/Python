import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

# 편식 리스트
hate_list = ['가지', '고사리', '김치', '당근', '무', '미나리', '미역', '버섯', '브로콜리', '연근', '오이', '콩', '피망', '호박', '채소']
datas = []

# 편식 리스트 검색 결과 돌리기
for hate in hate_list:
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    # 검색 결과 페이지 돌리기
    for num in range(1, 21):
        response = requests.get(f'https://www.10000recipe.com/recipe/list.html?q={hate}&order=reco&page={num}', headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')
        url_list = soup.select('.common_sp_list_li')
        num_list = []
        for url in url_list:
                num_list.append(url.a.get('href').split('/recipe/')[1])
        # 검색 결과 페이지에서 고유 url 숫자 가져오기
        for nu in num_list:
            headers1 = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            }

            response1 = requests.get(f'https://www.10000recipe.com/recipe/{nu}', headers=headers1)
            soup1 = BeautifulSoup(response1.content, 'html.parser')
            # 원하는 데이터 파싱
            try:
                data = json.loads(soup1.find('script', type='application/ld+json').text)
            except:
                pass
            # 데이터 형식 만들기
            try:
                data_info = []
                data_info.append(hate)
                data_info.append(data['name'])
                data_info.append(data['image'][1]) # 풀
                data_info.append(data['image'][0]) # 크롭
                data_info.append(data['description'])
                data_info.append(data['recipeIngredient'])
                data_info.append(data['recipeInstructions'])
                datas.append(data_info)
            except:
                pass

# 전체 리스트 df로 만들기
df = pd.DataFrame(datas,
               columns=['category', 'title', 'img', 'thumbnail', 'description', 'ingredient', 'step'])
# df csv파일로 만들기
df.to_csv('hate.csv', index=False, encoding='utf-8')