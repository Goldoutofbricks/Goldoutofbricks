import requests
url = 'http://www.njhouse.com.cn/2016/spf/'



response = requests.get(url)

print(response.text)

