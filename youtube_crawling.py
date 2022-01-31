# thanks to Kai Hong(kinghong97), Claire Chung
# 본인 쿠키 넣어야 함
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    'authority': 'www.youtube.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'x-origin': 'https://www.youtube.com',
    'authorization': 'SAPISIDHASH 1643360986_7406bbdeb20db2ed23d0bf27396e7706e58e56c8',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'x-goog-authuser': '0',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-full-version': '"97.0.4692.99"',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20220126.11.00',
    'content-type': 'application/json',
    'x-goog-visitor-id': 'CgtWd1VZVlp2aHZHQSi15c6PBg%3D%3D',
    'accept': '*/*',
    'origin': 'https://www.youtube.com',
    'x-client-data': 'CJS2yQEIpLbJAQjBtskBCKmdygEI2tHKAQjR88oBCOvyywEInvnLAQjnhMwBCIiVzAEI0JfMARitqcoB',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-dest': 'empty',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie':''
}

params = (
    ('key', 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
)
# 결과 저장
search_result = []
# 검색 퀴리 리스트 - 검색할 쿼리 여기에 넣어
query_list = ['자취요리', '자취청소','홈트레이닝','자취방구하기']
# 쿼리리스트로 for문 돌리기
for querys in query_list:
    query = f'{querys}&sp=CAMSBBABGAM%253D'
    data = '{"context":{"client":{"hl":"ko","gl":"KR","remoteHost":"122.46.193.231","deviceMake":"","deviceModel":"","visitorData":"CgtWd1VZVlp2aHZHQSi15c6PBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220126.11.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/results?search_query=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D","screenPixelDensity":1,"platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CLXlzo8GELvH_RIQgOqtBRC3y60FEJjqrQUQveutBRCDz60FEKPM_RIQst6tBRCR-PwSENi-rQU%3D"},"screenDensityFloat":1.25,"timeZone":"Asia/Seoul","browserName":"Chrome","browserVersion":"97.0.4692.99","screenWidthPoints":1536,"screenHeightPoints":746,"utcOffsetMinutes":540,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"/results?search_query=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clickTracking":{"clickTrackingParams":"CBwQ7VAiEwiYsd3PjNT1AhVNVYUKHW3ACIM="},"adSignalsInfo":{"params":[{"key":"dt","value":"1643360951026"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"540"},{"key":"u_his","value":"4"},{"key":"u_h","value":"864"},{"key":"u_w","value":"1536"},{"key":"u_ah","value":"816"},{"key":"u_aw","value":"1536"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"746"},{"key":"biw","value":"1520"},{"key":"brdim","value":"1919,215,1919,215,1536,216,1538,818,1536,746"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKrFqGCPI0vwuuoXen9chwU-zXUd5Lm29BfSJU66zAJtNBBmxJSJNEUF1yJYa3b4_T5FWPioKMedF_dNZfsaaUJDQa4Nlg"}},"query":"'+ query +'","webSearchboxStatsUrl":"/search?oq='+ query + '&gs_l=youtube.12...0.0.1.30787.0.0.0.0.0.0.0.0..0.0.uqrrle2,ytpso-bo-bro-e=1,ytpsoso-bo-bro-e=1.1..0...1ac..64.youtube..0.0.0....0.xXT5J35wozs"}'
    response = requests.post('https://www.youtube.com/youtubei/v1/search', headers=headers, params=params, data=data.encode('utf-8'))
    # json_res = json.loads(response.text)
    # response 제이슨화
    json_res = response.json()
    # url 저장
    list1 = []
    # response에서 url 얻기
    data = json_res['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']
    for b in data:
        try:
            c = b['itemSectionRenderer']['contents']
        except:
            continue
        for a in c:
            try:
                data2 = a['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
                list1.append(data2.split('=')[1])
            except:
                continue
            # 예외처리
            # try:
            #     if 'videoRenderer' in a:
            #         data2 = a['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            #         list1.append(data2.split('=')[1])
            #         # print(data2)
            #     elif 'shelfRenderer' in a:
            #         data2 = a['shelfRenderer']['content']['verticalListRenderer']['items']
            #         for zzzzz in data2:
            #             data222 = zzzzz['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            #             list1.append(data222.split('=')[1])
            #     elif 'radioRenderer' in a:
            #         for zzzzz in a['radioRenderer']['videos']:
            #             data222 = zzzzz['childVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata'][
            #                 'url']
            #             list1.append(data222.split('=')[1])
            #     elif 'playlistRenderer' in a:
            #         for zzzzz in a['playlistRenderer']['videos']:
            #             data222 = zzzzz['childVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata'][
            #                 'url']
            #             list1.append(data222.split('=')[1])
            # except:
            #     pass
    print(len(list1))
    # url로 유튜브에 post보내서 video detail 얻기
    for url in list1:
        video_detail = []
        headers11 = {
            'authority': 'www.youtube.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'x-origin': 'https://www.youtube.com',
            'authorization': 'SAPISIDHASH 1643360986_7406bbdeb20db2ed23d0bf27396e7706e58e56c8',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'x-goog-authuser': '0',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-model': '',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'sec-ch-ua-full-version': '"97.0.4692.99"',
            'x-youtube-client-name': '1',
            'x-youtube-client-version': '2.20220126.11.00',
            'content-type': 'application/json',
            'x-goog-visitor-id': 'CgtWd1VZVlp2aHZHQSi15c6PBg%3D%3D',
            'accept': '*/*',
            'origin': 'https://www.youtube.com',
            'x-client-data': 'CJS2yQEIpLbJAQjBtskBCKmdygEI2tHKAQjR88oBCOvyywEInvnLAQjnhMwBCIiVzAEI0JfMARitqcoB',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-dest': 'empty',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': ''
        }

        # params = (
        #     ('key', 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
        # )

        # query = '자취요리&sp=CAMSAhgD'
        # url = 'YlKg2Uc1HPQ'
        # json에 f string 넣기
        data11 = f'|"context":|"client":|"hl":"ko","gl":"KR","remoteHost":"14.53.186.145","deviceMake":"","deviceModel":"","visitorData":"CgtyVTgxcTFuNURGMCjQ19uPBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220127.09.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/watch?v={url}?","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":|"appInstallData":"CNDX248GELfLrQUQveutBRC7x_0SEIDqrQUQmOqtBRCU8a0FENzN_RIQ2L6tBRCR-PwS"?,"timeZone":"Asia/Seoul","browserName":"Chrome","browserVersion":"97.0.4692.99","screenWidthPoints":1920,"screenHeightPoints":937,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":540,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","memoryTotalKbytes":"8000000","clientScreen":"WATCH","mainAppWebInfo":|"graftUrl":"/watch?v={url}","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true??,"user":|"lockedSafetyMode":false?,"request":|"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]?,"clickTracking":|"clickTrackingParams":"CIUBENwwGAUiEwiy1Ye-n9r1AhX0QQ8CHUAbCP8yBnNlYXJjaFIM7J6Q7Leo7JqU66asmgEDEPQk"?,"adSignalsInfo":|"params":[|"key":"dt","value":"1643572170912"?,|"key":"flash","value":"0"?,|"key":"frm","value":"0"?,|"key":"u_tz","value":"540"?,|"key":"u_his","value":"28"?,|"key":"u_h","value":"1080"?,|"key":"u_w","value":"1920"?,|"key":"u_ah","value":"1040"?,|"key":"u_aw","value":"1920"?,|"key":"u_cd","value":"24"?,|"key":"bc","value":"31"?,|"key":"bih","value":"937"?,|"key":"biw","value":"1904"?,|"key":"brdim","value":"0,0,0,0,1920,0,1920,1040,1920,937"?,|"key":"vis","value":"1"?,|"key":"wgl","value":"true"?,|"key":"ca_type","value":"image"?],"bid":"ANyPxKq7oaoDEDd4pMNsOta7fbLGSLmS47v5JwktDuMGClo3XTWy5k5cxeMz7EbFQXcrzEtPAGx6q0j0hMBqdnTfoyB-OgoxSg"??,"videoId":"{url}","playbackContext":|"contentPlaybackContext":|"currentUrl":"/watch?v={url}","vis":0,"splay":false,"autoCaptionsDefaultOn":false,"autonavState":"STATE_NONE","html5Preference":"HTML5_PREF_WANTS","signatureTimestamp":19019,"lactMilliseconds":"-1"??,"racyCheckOk":false,"contentCheckOk":false?'
        change1 = data11.replace("|", "{")
        change2 = change1.replace("?", "}")

        response11 = requests.post('https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
                                 headers=headers11, params=params, data=change2.encode('utf-8'))
        # response 디코딩
        json_res11 = response11.content.decode()
        # 디코딩된거 json화
        data111 = json.loads(json_res11)
        video_detail.append(querys)
        # video detail에서 하나씩 뽑아서 리스트에 저장하기

        video_detail.append(data111['videoDetails']['videoId'])
        video_detail.append(data111['videoDetails']['title'])
        try:
            video_detail.append(data111['videoDetails']['keywords'])
        except:
            video_detail.append('')
        video_detail.append(data111['videoDetails']['thumbnail']['thumbnails'][3]['url'])
        video_detail.append(data111['videoDetails']['shortDescription'])

        # 한 리스트를 전체 리스트에 넣기
        search_result.append(video_detail)
# 전체 리스트 df로 만들기
df = pd.DataFrame(search_result,
               columns=['category', 'videoId', 'title', 'keywords', 'thumbnail', 'description'])
# df csv파일로 만들기
df.to_csv('youtube_data.csv', index=False, encoding='utf-8')