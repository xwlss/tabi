import requests
import time
from  faker  import  Faker

with open('./tabi.txt', "r") as f:
    
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
            #本处根据你的地址私钥文件格式进行修改
            #如果文件中仅有地址：
            'address': i.strip(),
            #如果文件中以地址：私钥形式：
            #'address': i.split(':')[0],
            #如果文件中以私钥，地址形式：
            #'address': i.split(',')[1].strip(),
        }
    
        #更新代理 需要自行购买或者配置 目前市场上很多 大家按自己需要使用
        #以nstproxy示例 
        #在nstproxy网站上注册获取 nstproxy_Channel 和 nstproxy_Password
        #nstproxy_Channel='XXX'
        #nstproxy_Password='XXX'
        #nstproxies = f"http://{nstproxy_Channel}-residential-country_ANY-r_5m-s_BsqLCLkiVu:{nstproxy_Password}@gw-us.nstproxy.com:24125"
        #proxies = {'all://': nstproxy}
        proxies = {'all://': 'http://127.0.0.1:12345'}#以你的代理服务网址或ip和端口替换127.0.0.1:12345
        
        response = requests.post('https://faucet-api.testnet.tabichain.com/api/faucet', headers=headers, json=json_data,verify=False,proxies=proxies)
        print(response.text)
        if response.status_code!=200:
            time.sleep(50)
