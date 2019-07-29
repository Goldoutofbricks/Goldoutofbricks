#获取www.nanjinghouse.com.cn当天的认购数量/成交数量

import requests
import csv
import datetime

url = "http://www.njhouse.com.cn/2016/spf/getdata.php"

headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cache-Control': "max-age=0",
    'Connection': "keep-alive",
    'Cookie': "bdshare_firstime=1528132548786; PHPSESSID=qbm6gcti3hf9k1627in1n42cl4; guid=667444079; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1, bdshare_firstime=1528132548786; PHPSESSID=qbm6gcti3hf9k1627in1n42cl4; guid=667444079; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; PHPSESSID=62t5u83v3s862liath409hrjq7",
    'Host': "www.njhouse.com.cn",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    'Postman-Token': "e86192be-c62f-4769-80c7-e5476b84625b,3e5a05e3-50e4-422d-8936-376ea3669041",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

today = datetime.date.today()

Headers = ['Date','NanjingDailyNewOrder','NanjingDailyNewDeal']
rows = [today,response.text,response.text]

with open('NanjingDailyNewDeal.csv','w') as filecsv:
        filecsv_csv = csv.writer(filecsv)
        filecsv_csv.writerow(headers)
        filecsv_csv.writerows(rows)
