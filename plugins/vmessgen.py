from pyxui import XUI
from pyxui.config_gen import config_generator
import uuid
import time
import datetime
import json
import msg as server
import random
# Advanced:

Gcp = XUI(
    full_address="http://62.77.159.102:8888",
    panel="alireza", # Your panel name, "alireza" or "sanaei"
    https=False, # Make note if you don't use https set False else set True
    session_string="MTY5MDI3Mzc0MXxEdi1CQkFFQ180SUFBUkFCRUFBQV83WF9nZ0FCQm5OMGNtbHVad3dNQUFwTVQwZEpUbDlWVTBWU0dIZ3RkV2t2WkdGMFlXSmhjMlV2Ylc5a1pXd3VWWE5sY3YtREF3RUJCRlZ6WlhJQl80UUFBUWdCQWtsa0FRUUFBUWhWYzJWeWJtRnRaUUVNQUFFSVVHRnpjM2R2Y21RQkRBQUJDMDkwY0Y5bGJtRmliR1ZrQVFJQUFReFBkSEJmZG1WeWFXWnBaV1FCQWdBQkNrOTBjRjl6WldOeVpYUUJEQUFCREU5MGNGOWhkWFJvWDNWeWJBRU1BQUVLVDNSd1gzRnlZMjlrWlFFS0FBQUFHdi1FRndFQ0FRaHRiMlJ6WW05MGN3RUliVzlrYzJKdmRITUF8oMlk74d2-ZC7mlk-MxxWQh0ce2PtTvDAJskmWsU8pTk="
)
Atom = XUI(
    full_address="http://atom.modsbots.com:8888",
    panel="sanaei", # Your panel name, "alireza" or "sanaei"
    https=False, # Make note if you don't use https set False else set True
    session_string="MTY5MTQxMzE4OHxEdi1CQkFFQ180SUFBUkFCRUFBQWRmLUNBQUVHYzNSeWFXNW5EQXdBQ2t4UFIwbE9YMVZUUlZJWWVDMTFhUzlrWVhSaFltRnpaUzl0YjJSbGJDNVZjMlZ5XzRNREFRRUVWWE5sY2dIX2hBQUJCQUVDU1dRQkJBQUJDRlZ6WlhKdVlXMWxBUXdBQVFoUVlYTnpkMjl5WkFFTUFBRUxURzluYVc1VFpXTnlaWFFCREFBQUFCcl9oQmNCQWdFSWJXOWtjMkp2ZEhNQkNHMXZaSE5pYjNSekFBPT18ECRzacXR3qVhpqBB7sJLuC4jSSwgq7oloZqho2FJBME="
)
def uuidgen():
    myuuid = uuid.uuid4()
    return myuuid 

def key_gen(id,amt,sv,port,tls,type,op):# tls == tls or /
    config = {
    "v": "2",
    "ps": f"modsbots.com-{amt}-{op}",
    "add": sv,
    "port": port,
    "id": id,
    "aid": "0",
    "scy": "auto",
    "net": type,
    "type": type,
    "host": "",
    "path": tls,
    "tls": "",
    "sni": "",
    "alpn": "h2,http/1.1",
    "fp": "chrome"
}

    generate_config = config_generator("vmess", config)
    return generate_config
def vmess_acc_create(userid,opt):
    if opt == "Atom":
        choicess =  ['3368709120','2368709120']   #['5368709120','4368709120','3368709120','2368709120']
        freedata = random.choice(choicess)
        if freedata == '5368709120':
            amt = "5GB"
        elif freedata == '4368709120':
            amt = "4GB"
        elif freedata == '3368709120':
            amt = "3GB"
        elif freedata == '2368709120':
            amt = "2GB"
        d = datetime.datetime.now()
        unixtime = datetime.datetime.timestamp(d)*1000
        end_timestamp = int(unixtime) + 86400*1000
        try:
            today = datetime.date.today()
            myuuid = uuid.uuid4()
            get = Atom.add_client(
            inbound_id=1,
            email=f"{userid}@atom.modsbots.com",
            uuid=str(myuuid),
            enable = True,
            flow = "",
            limit_ip = 0,
            total_gb = int(freedata),
            expire_time =end_timestamp, # You must pass 13 digit timestamp
            telegram_id = "",
            subscription_id = ""    
            )
            sv = "atom.modsbots.com"
            port = "4000"
            tls = "/"
            type = "tcp"
            op = 'ATOM'
            vmess_key = key_gen(str(myuuid),amt,sv,port,tls,type,op)
            f = open(f'users/{userid}.json')
            data = json.load(f)  
            data["D_Free_Date"] = str(today)
            data["D_Free_Id"] = str(myuuid)
            data["D_Free_key"] = vmess_key

            with open(f'users/{userid}.json', "w") as jsonFile:
                json.dump(data, jsonFile)    

            return vmess_key, amt

        except:
            return "kmkl"
  
def vmess_acc_create_earn(userid):
    d = datetime.datetime.now()
    unixtime = datetime.datetime.timestamp(d)*1000
    end_timestamp = int(unixtime) + 86400*1000
    myuuid = uuid.uuid4()
    try:
        today = datetime.date.today()
       
        get = Atom.add_client(
        inbound_id=1,
        email=f"{userid}@earn.atom.modsbots.com",
        uuid=str(myuuid),
        enable = True,
        flow = "",
        limit_ip = 0,
        total_gb = 3368709120,
        expire_time =end_timestamp, # You must pass 13 digit timestamp
        telegram_id = "",
        subscription_id = ""    
        )
        amt = "3GB"
        sv = "atom.modsbots.com"
        port = "4000"
        tls = "/"
        type = "tcp"
        op = "ATOM"
        vmess_key = key_gen(str(myuuid),amt,sv,port,tls,type,op)
        #vmess_key = key_gen(str(myuuid),amt)
        f = open(f'users/{userid}.json')
        data = json.load(f)  
        ref = data['Ref']
        data["D_Earn_Date"] = str(today)
        data["D_Earn_Id"] = str(myuuid)
        data["D_Earn_key"] = vmess_key
        data['Ref'] = ref - 3000

        with open(f'users/{userid}.json', "w") as jsonFile:
            json.dump(data, jsonFile)    

        return vmess_key

    except:
        return "kmkl"
       
def deleteVmessfree(userid,opt):
    if opt == "Atom":
        get_client = Atom.delete_client(
        inbound_id=1,
        email=f"{userid}@atom.modsbots.com",
    # Make note you don't have to pass both of them (email, uuid), just one is enough
        )
def deleteVmessearn(userid,opt):
    if opt == "Atom":
        get_client = Atom.delete_client(
        inbound_id=1,
        email=f"{userid}@earn.atom.modsbots.com",
    # Make note you don't have to pass both of them (email, uuid), just one is enough
        )
