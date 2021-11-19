import requests

proxy_url = "http://proxy-rest.awsnx.wisers.com.cn/proxy/zhima"

test_url = "http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId=904925&itemId=915"
test_keys = ["三是强化内控管理"]


def validate_proxy(request_url: str, proxy: str):
    result = False
    try:
        proxies = {
            'http': proxy,
            'https': proxy,
        }
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'

        }
        res = requests.get(request_url, proxies=proxies, headers=headers, timeout=20)
        result = res.status_code == 200 and len(res.text) > 1000
    except:
        pass
    return result


def get_proxy():
    proxy_data = requests.get(proxy_url).json()
    return proxy_data.get('proxy')


def tt_proxy(proxy):
    return validate_proxy(test_url, proxy)


result = {
    "succeed": 0,
    "failed": 0
}
for i in range(100):

    proxy = get_proxy()
    succeed = tt_proxy(proxy)
    if succeed:
        result['succeed'] = result['succeed'] + 1
    else:
        result['failed'] = result['failed'] + 1
    print("{} \t {} \t {}".format(i, proxy, succeed))

print(result)
