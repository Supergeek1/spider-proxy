import requests

proxy_url = "http://proxy-rest.awsnx.wisers.com.cn/proxy/zhima"

test_url = "http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId=904925&itemId=915"
test_keys = ["三是强化内控管理"]


def validate_proxy(request_url: str, proxy: str):
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    headers = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'

    }
    res = requests.get(request_url, proxies=proxies, headers=headers, timeout=10)
    return res.status_code == 200




for i in range(100):

    print("{} \t {} \t {}".format(i, 1, 4))
