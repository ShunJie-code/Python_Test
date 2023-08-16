import requests
import json

url = "https://api.bilibili.com/x/player/pagelist?bvid=BV1jW411K7yg&jsonp=jsonp"
res = requests.get(url)
if res.status_code == 200:
    js = json.loads(res.text)
    with open('小甲鱼数据结构.txt', 'a') as f:
        for x in js.get('data'):
            f.write('P' + str(x.get('page')) + ' ' + x.get('part') + '\n')
