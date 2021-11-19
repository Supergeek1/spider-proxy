import time

import requests


def read_ips(file_path) -> set:
    f = open(file_path, 'r', encoding='utf-8')
    result = set()
    for line in f.readlines():
        if line and '.' in line:
            result.add(line.strip().replace('\n', ''))
    print('read {} ip from {}'.format(len(result), file_path))
    f.close()
    return result


#save_api = "http://wapi.http.cnapi.cc/index/index/save_white?neek=65140&appkey=76230a3ac6abe1a1b355a26d0f8b8735&white={}"
save_api = "http://wapi.http.linkudp.com/index/index/save_white?neek=65140&appkey=76230a3ac6abe1a1b355a26d0f8b8735&white={}"


def save_white_list(ip):
    try:
        res = requests.get(save_api.format(ip))
        return res.json()['msg']
    except:
        return 'save_failed'


file_ip = 'icp2-crawler-20201225.txt'
ips = read_ips(file_ip)
size = len(ips)
i = 0
for ip in ips:
    msg = save_white_list(ip)
    i = i + 1
    print('[{}/{}]\t{}\t{}'.format(i, size, ip, msg))
    time.sleep(5)
