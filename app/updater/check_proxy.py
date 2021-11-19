# -*- coding: utf-8 -*-
from pprint import pprint

import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.baidu.com'

proxy_str = '''
http://162565:162565@ip3.hahado.cn:42997
http://162537:162537@ip3.hahado.cn:42969
http://162564:162564@ip3.hahado.cn:42996
http://162571:162571@ip3.hahado.cn:43003
http://162536:162536@ip3.hahado.cn:42968
http://162538:162538@ip3.hahado.cn:42970
http://162548:162548@ip3.hahado.cn:42980
http://162551:162551@ip3.hahado.cn:42983
http://162555:162555@ip3.hahado.cn:42987
http://162560:162560@ip3.hahado.cn:42992
http://162561:162561@ip3.hahado.cn:42993
http://162570:162570@ip3.hahado.cn:43002
http://162576:162576@ip3.hahado.cn:43008
http://162575:162575@ip3.hahado.cn:43007
http://162574:162574@ip3.hahado.cn:43006
http://162550:162550@ip3.hahado.cn:42982
http://162539:162539@ip3.hahado.cn:42971
http://162540:162540@ip3.hahado.cn:42972
http://162541:162541@ip3.hahado.cn:42973
http://162542:162542@ip3.hahado.cn:42974
http://162543:162543@ip3.hahado.cn:42975
http://162544:162544@ip3.hahado.cn:42976
http://162545:162545@ip3.hahado.cn:42977
http://162546:162546@ip3.hahado.cn:42978
http://162547:162547@ip3.hahado.cn:42979
http://162549:162549@ip3.hahado.cn:42981
http://162552:162552@ip3.hahado.cn:42984
http://162553:162553@ip3.hahado.cn:42985
http://162554:162554@ip3.hahado.cn:42986
http://162558:162558@ip3.hahado.cn:42990
http://162559:162559@ip3.hahado.cn:42991
http://162562:162562@ip3.hahado.cn:42994
http://162563:162563@ip3.hahado.cn:42995
http://162566:162566@ip3.hahado.cn:42998
http://162567:162567@ip3.hahado.cn:42999
http://162568:162568@ip3.hahado.cn:43000
http://162569:162569@ip3.hahado.cn:43001
http://162572:162572@ip3.hahado.cn:43004
http://162573:162573@ip3.hahado.cn:43005
http://162577:162577@ip3.hahado.cn:43009
http://162578:162578@ip3.hahado.cn:43010
http://162579:162579@ip3.hahado.cn:43011
http://162580:162580@ip3.hahado.cn:43012
http://162581:162581@ip3.hahado.cn:43013
http://162582:162582@ip3.hahado.cn:43014
http://162583:162583@ip3.hahado.cn:43015
http://162584:162584@ip3.hahado.cn:43016
http://162585:162585@ip3.hahado.cn:43017
http://162599:162599@ip3.hahado.cn:43031
http://162629:162629@ip3.hahado.cn:43061
http://162600:162600@ip3.hahado.cn:43032
http://162623:162623@ip3.hahado.cn:43055
http://162621:162621@ip3.hahado.cn:43053
http://162617:162617@ip3.hahado.cn:43049
http://162614:162614@ip3.hahado.cn:43046
http://162588:162588@ip3.hahado.cn:43020
http://162587:162587@ip3.hahado.cn:43019
http://162609:162609@ip3.hahado.cn:43041
http://162613:162613@ip3.hahado.cn:43045
http://162622:162622@ip3.hahado.cn:43054
http://162634:162634@ip3.hahado.cn:43066
http://162589:162589@ip3.hahado.cn:43021
http://162590:162590@ip3.hahado.cn:43022
http://162591:162591@ip3.hahado.cn:43023
http://162592:162592@ip3.hahado.cn:43024
http://162593:162593@ip3.hahado.cn:43025
http://162594:162594@ip3.hahado.cn:43026
http://162595:162595@ip3.hahado.cn:43027
http://162596:162596@ip3.hahado.cn:43028
http://162597:162597@ip3.hahado.cn:43029
http://162598:162598@ip3.hahado.cn:43030
http://162601:162601@ip3.hahado.cn:43033
http://162602:162602@ip3.hahado.cn:43034
http://162603:162603@ip3.hahado.cn:43035
http://162604:162604@ip3.hahado.cn:43036
http://162605:162605@ip3.hahado.cn:43037
http://162606:162606@ip3.hahado.cn:43038
http://162610:162610@ip3.hahado.cn:43042
http://162611:162611@ip3.hahado.cn:43043
http://162612:162612@ip3.hahado.cn:43044
http://162615:162615@ip3.hahado.cn:43047
http://162616:162616@ip3.hahado.cn:43048
http://162618:162618@ip3.hahado.cn:43050
http://162619:162619@ip3.hahado.cn:43051
http://162620:162620@ip3.hahado.cn:43052
http://162624:162624@ip3.hahado.cn:43056
http://162625:162625@ip3.hahado.cn:43057
http://162626:162626@ip3.hahado.cn:43058
http://162627:162627@ip3.hahado.cn:43059
http://162628:162628@ip3.hahado.cn:43060
http://162630:162630@ip3.hahado.cn:43062
http://162631:162631@ip3.hahado.cn:43063
http://162632:162632@ip3.hahado.cn:43064
http://162633:162633@ip3.hahado.cn:43065
http://162635:162635@ip3.hahado.cn:43067
http://162636:162636@ip3.hahado.cn:43068
http://162679:162679@ip5.hahado.cn:43111
http://162655:162655@ip5.hahado.cn:43087
http://162662:162662@ip5.hahado.cn:43094
http://162663:162663@ip5.hahado.cn:43095
http://162665:162665@ip5.hahado.cn:43097
http://162661:162661@ip5.hahado.cn:43093
http://162677:162677@ip5.hahado.cn:43109
http://162664:162664@ip5.hahado.cn:43096
http://162687:162687@ip5.hahado.cn:43119
http://162649:162649@ip5.hahado.cn:43081
http://162650:162650@ip5.hahado.cn:43082
http://162651:162651@ip5.hahado.cn:43083
http://162652:162652@ip5.hahado.cn:43084
http://162653:162653@ip5.hahado.cn:43085
http://162654:162654@ip5.hahado.cn:43086
http://162656:162656@ip5.hahado.cn:43088
http://162657:162657@ip5.hahado.cn:43089
http://162658:162658@ip5.hahado.cn:43090
http://162659:162659@ip5.hahado.cn:43091
http://162660:162660@ip5.hahado.cn:43092
http://162666:162666@ip5.hahado.cn:43098
http://162667:162667@ip5.hahado.cn:43099
http://162668:162668@ip5.hahado.cn:43100
http://162669:162669@ip5.hahado.cn:43101
http://162670:162670@ip5.hahado.cn:43102
http://162673:162673@ip5.hahado.cn:43105
http://162674:162674@ip5.hahado.cn:43106
http://162675:162675@ip5.hahado.cn:43107
http://162676:162676@ip5.hahado.cn:43108
http://162678:162678@ip5.hahado.cn:43110
http://162680:162680@ip5.hahado.cn:43112
http://162681:162681@ip5.hahado.cn:43113
http://162682:162682@ip5.hahado.cn:43114
http://162683:162683@ip5.hahado.cn:43115
http://162684:162684@ip5.hahado.cn:43116
http://162685:162685@ip5.hahado.cn:43117
http://162686:162686@ip5.hahado.cn:43118
http://162688:162688@ip5.hahado.cn:43120
http://162689:162689@ip5.hahado.cn:43121
http://162690:162690@ip5.hahado.cn:43122
http://162691:162691@ip5.hahado.cn:43123
http://162692:162692@ip5.hahado.cn:43124
http://162693:162693@ip5.hahado.cn:43125
http://162694:162694@ip5.hahado.cn:43126
http://162695:162695@ip5.hahado.cn:43127
http://162696:162696@ip5.hahado.cn:43128
http://162697:162697@ip5.hahado.cn:43129
http://162698:162698@ip5.hahado.cn:43130
http://162729:162729@ip5.hahado.cn:43161
http://162727:162727@ip5.hahado.cn:43159
http://162728:162728@ip5.hahado.cn:43160
http://162730:162730@ip5.hahado.cn:43162
http://162731:162731@ip5.hahado.cn:43163
http://162732:162732@ip5.hahado.cn:43164
http://162715:162715@ip5.hahado.cn:43147
http://162705:162705@ip5.hahado.cn:43137
http://162708:162708@ip5.hahado.cn:43140
http://162716:162716@ip5.hahado.cn:43148
http://162717:162717@ip5.hahado.cn:43149
http://162707:162707@ip5.hahado.cn:43139
http://162702:162702@ip5.hahado.cn:43134
http://162703:162703@ip5.hahado.cn:43135
http://162704:162704@ip5.hahado.cn:43136
http://162706:162706@ip5.hahado.cn:43138
http://162709:162709@ip5.hahado.cn:43141
http://162710:162710@ip5.hahado.cn:43142
http://162711:162711@ip5.hahado.cn:43143
http://162712:162712@ip5.hahado.cn:43144
http://162713:162713@ip5.hahado.cn:43145
http://162714:162714@ip5.hahado.cn:43146
'''

proxy_list = [
              'http://148558:148558@ip3.hahado.cn:48936',
              'http://148559:148559@ip3.hahado.cn:48937',
              'http://148560:148560@ip3.hahado.cn:48938',
              'http://148561:148561@ip3.hahado.cn:48939',
              'http://148562:148562@ip3.hahado.cn:48940',
              'http://148563:148563@ip3.hahado.cn:48941',
              'http://148564:148564@ip3.hahado.cn:48942',
              'http://148565:148565@ip3.hahado.cn:48943',
              'http://148566:148566@ip3.hahado.cn:48944',
              'http://148567:148567@ip3.hahado.cn:48945',
              'http://148568:148568@ip3.hahado.cn:48946',
              'http://148569:148569@ip3.hahado.cn:48947',
              'http://148570:148570@ip3.hahado.cn:48948',
              'http://148571:148571@ip3.hahado.cn:48949',
              'http://148572:148572@ip3.hahado.cn:48950',
              'http://126880:126880@ip5.hahado.cn:47204',
              'http://126881:126881@ip5.hahado.cn:47205',
              'http://151651:151651@ip5.hahado.cn:42056',
              'http://126884:126884@ip5.hahado.cn:47208',
              'http://135596:135596@ip5.hahado.cn:45947',
              'http://148573:148573@ip5.hahado.cn:48951',
              'http://148574:148574@ip5.hahado.cn:48952',
              'http://148575:148575@ip5.hahado.cn:48953',
              'http://148576:148576@ip5.hahado.cn:48954',
              'http://148577:148577@ip5.hahado.cn:48955',
              'http://148578:148578@ip5.hahado.cn:48956',
              'http://151652:151652@ip5.hahado.cn:42057',
              'http://148580:148580@ip5.hahado.cn:48958',
              'http://148581:148581@ip5.hahado.cn:48959',
              'http://148582:148582@ip5.hahado.cn:48960',
              'http://148583:148583@ip5.hahado.cn:48961',
              'http://148584:148584@ip5.hahado.cn:48962',
              'http://148585:148585@ip5.hahado.cn:48963',
              'http://148586:148586@ip5.hahado.cn:48964',
              'http://148587:148587@ip5.hahado.cn:48965',


]

check_url = 'http://%s/simple/current-ip?username=%s&password=%s'
restart_url = 'http://%s/simple/update?username=%s&password=%s'
switch_url = 'http://%s/simple/switch-ip?username=%s&password=%s'

ip_pool = {}


def check(check_list):
    error_list = []
    i = 0

    squid_conf = ''

    for proxy in check_list:
        if not proxy:
            continue
        split_url = proxy.replace('http://', '')
        username = split_url.split('@')[0].split(':')[0]
        password = split_url.split('@')[0].split(':')[1]
        host = split_url.split('@')[1].split(':')[0]
        port = split_url.split('@')[1].split(':')[1]

        squid_conf += 'cache_peer ' + host + ' parent ' + port + ' 0 login=' + username + ':' + password + ' no-digest no-query weighted-round-robin weight=1 connect-fail-limit=20 allow-miss max-conn=50 name=proxy-' + str(
            i)
        squid_conf += '\n'
        i += 1
        # print('check', proxy)
        start = time.time()
        proxies = {'http': proxy, 'https': proxy}
        try:
            # response = requests.get(switch_url % (host, username, password))
            # print(response.json())

            # response = requests.get(restart_url % (host, username, password))
            # print(response.json())

            response = requests.get(url, proxies=proxies, timeout=10)
            response = requests.get(check_url % (host, username, password))
            if len(response.json()) > 0:
                ip = response.json()[0]['ip']
                ttl = response.json()[0]['ttl']
                print(proxy, ip, float(ttl) / 60)
            else:
                error_list.append(proxy)
                print(proxy, response.content)

            # ip_area = 'http://ip.tool.chinaz.com/%s' %ip
            # area = None
            # response = requests.post(ip_area)
            # area = BeautifulSoup(response.content, 'lxml').find_all('span', class_='Whwtdhalf w50-0')[-1].text

        except (requests.exceptions.ProxyError, requests.exceptions.Timeout, requests.exceptions.SSLError,
                requests.exceptions.ConnectionError) as e:
            print(proxy, '--------Error', e)
            error_list.append(proxy)
            continue
        # print(proxy, '--------Pass, takes', (time.time() - start))
    # print(squid_conf)

    return error_list


def check_error(check_list):
    if len(check_list) > 0:
        print('Check error list of length:%s ...' % len(check_list))
        time.sleep(1)
        error_list = check(check_list)
        print('Recheck error list of length:%s ...' % len(error_list))
        # restart_error(error_list)


def restart_error(check_list):
    if len(check_list) > 0:
        for proxy in check_list:
            split_url = proxy.replace('http://', '')
            username = split_url.split('@')[0].split(':')[0]
            password = split_url.split('@')[0].split(':')[1]
            host = split_url.split('@')[1].split(':')[0]
            port = split_url.split('@')[1].split(':')[1]
            print('restart', proxy)
            response = requests.get(restart_url % (host, username, password))
            print(response.content.strip())

    time.sleep(10)
    check(check_list)


if __name__ == '__main__':
    _list = check(proxy_str.split('\n'))
    _list = check(proxy_list)
    print('                <<<<<<<>>>>>>>>>>>>>')
    check_error(_list)
