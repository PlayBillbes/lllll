import requests
import random

def cf_crawl():
    links = [
        'https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/main/config.txt',
        'https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt',
        'https://raw.githubusercontent.com/m3hdio1/v2ray_sub/main/v2ray_sub.txt',
        'https://raw.githubusercontent.com/coldwater-10/V2Hub2/main/merged'
        
    ]
    cf = []
    for link in links:
       raw = requests.get(link).text
       raw = raw.splitlines()
       for p in raw:
            p_low = p.lower()
            if 'pages.dev' in p_low:
                cf.append(p)
            
            else:
               pass
    ran = random.choice(cf)
    vless, lastName = ran.split('#', -1)
    
    final = vless + "#Tg@ModsBots_Tech"
    
    return final
