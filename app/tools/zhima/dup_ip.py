def read_ips(file_path) -> set:
    f = open(file_path, 'r', encoding='utf-8')
    result = set()
    for line in f.readlines():
        if line and '.' in line:
            result.add(line.strip().replace('\n', ''))
    print('read {} ip from {}'.format(len(result), file_path))
    f.close()
    return result


file_ip = 'icp2-nx-puppeteer.txt'
ips = read_ips(file_ip)
for ip in ips:
    print(ip)
