import requests
import random
import string
import json
#STATUS = "active"
#res =  requests.get(f"http://62.77.159.102:8081/api/{token}/listuser/{STATUS}")

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def ssh_free_gen(api,token,userid,today):

    addapi = f"http://{api}:8081/api/adduser"
    passwd = get_random_string(6)
    payloads = {
        'token' : token,
        'username' : userid,
        'password' : passwd,
        'email' : 'gg@gg.com',
        'mobile' : '123654',
        'multiuser' : '1',
        'traffic' : '2',
        'type_traffic' : 'gb',
        'connection_start' : '1'  
    }
    res = requests.post(addapi,data = payloads)
    ress = res.content.decode()
    data = json.loads(ress)
    us = data['message']

    f = open(f'users/{userid}.json')
    data = json.load(f)
    pre = data['D_Free_Id']
    data["D_Free_key"] = passwd
    data["D_Free_Date"] = str(today)
    data["D_Free_Id"] = int(userid)
    with open(f'users/{userid}.json', "w") as jsonFile:
        json.dump(data, jsonFile)

    return us,passwd