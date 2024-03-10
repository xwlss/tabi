import requests
import time
from  faker  import  Faker
from eth_account import Account


Account.enable_unaudited_hdwallet_features()

n=100
for i in range(n):
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
        
        account, mnemonic = Account.create_with_mnemonic()
        print(mnemonic)
        address=account.address
        print(f'address: {address}, pk: 0x{account.key.hex()}')
        json_data = {
            'address': address,
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
        else:
                filename = "./tabi.txt"
                with open(filename, "a") as f:
                    f.writelines(account.address+','+account.key.hex()+','+mnemonic+'\n')
        
