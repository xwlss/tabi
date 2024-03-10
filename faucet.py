import requests
import time
from  faker  import  Faker

with open('./bera0.txt', "r") as f:
    content = f.readlines()
for i in content:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://faucet.testnet.tabichain.com',
            'Referer': 'https://faucet.testnet.tabichain.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': Faker().chrome(),#'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            #'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }
        json_data = {
            'address': i.split(',')[0],
        }
        r=requests.get('https://api.ake.net/refresh/-all-country-CA/23amv023d0')
        print(r.text)
        
        response = requests.post('https://faucet-api.testnet.tabichain.com/api/faucet', headers=headers, json=json_data,verify=False,proxies={'all':'http://150.230.176.82:24014'})
        print(response.text)
        if response.status_code!=200:
            time.sleep(50)
