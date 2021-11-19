from util.redis_util import RedisUtil
from validator.proxy_validate import ProxyValidator
test_url = "http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId=904925&itemId=915"
test_keys = ["三是强化内控管理"]
f = open("hk_proxy.txt")
#
redis_queues = ["rest:queue:all", "rest:queue:c4", "rest:queue:app", "rest:queue:hk", "rest:queue:hkex",
                "rest:queue:five"]

redis_queues = ["rest:queue:hk_wisers"]

#redis_queues = ["rest:queue:ofixed"]

### cn_bj
#redis_client = RedisUtil.get_redis_client('54.223.69.52', 30478, 0)

### cn_nx_icp2
#redis_client = RedisUtil.get_redis_client('10.19.251.219', 30163, 0)


## us
redis_client = RedisUtil.get_redis_client('10.3.1.65', 30163, 0)


def update_proxy(proxy_str):
    for queue in redis_queues:
        pipeline = redis_client.pipeline()
        pipeline.zadd(queue, {proxy_str: 9999})
        pipeline.execute()


def del_proxy(proxy_str):
    for queue in redis_queues:
        pipeline = redis_client.pipeline()
        pipeline.zrem(queue, proxy_str)
        pipeline.execute()


lines = f.readlines()
for proxy in lines:
    if 'http' not in proxy:
        proxy = "http://" + proxy.strip()
    else:
        proxy = proxy.strip()
    #succeed = ProxyValidator.validate_proxy(test_url, proxy, test_keys)
    #if succeed:
    if True:
        update_proxy(proxy.strip())
        print(proxy + "\t    succeed..")
    else:
        print(proxy + "\t    failed  !!")

# del_proxy("http://ydrnpyytmc:u4ZCdnrlZ2Hbn@ip5.hahado.cn:31208")
print("update done!!")
