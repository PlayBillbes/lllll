import json
import servers as server
from outline_vpn.outline_vpn import OutlineVPN

def create_outline_user_free(ip,token,userid,today,country):
    client = OutlineVPN(api_url=ip,
        cert_sha256=token)
    
    f = open(f'users/{userid}.json')
    data = json.load(f)   
    #client.delete_key(int(D_Free_Id))

    new_key = client.create_key()
    id = new_key.key_id
    ss = new_key.access_url + f"#-2GB-FREE-{country}" 
    client.add_data_limit(new_key.key_id, 1000 * 1000 * 2000)

    data["D_Free_Date"] = str(today)
    data["D_Free_Id"] = id
    data["D_Free_key"] = ss

    with open(f'users/{userid}.json', "w") as jsonFile:
        json.dump(data, jsonFile)
    return ss

def create_outline_user_earn(ip,token,userid,today,country):
    client = OutlineVPN(api_url=ip,
        cert_sha256=token)
    
    f = open(f'users/{userid}.json')
    data = json.load(f)   
    #client.delete_key(int(D_Free_Id))
    ref = data['Ref']
    new_key = client.create_key()
    id = new_key.key_id
    ss = new_key.access_url + f"#-3GB-FREE-{country}" 
    client.add_data_limit(new_key.key_id, 1000 * 1000 * 3000)

    data["D_Earn_Date"] = str(today)
    data["D_Earn_Id"] = id
    data["D_Earn_key"] = ss
    data['Ref'] = ref - 3000

    with open(f'users/{userid}.json', "w") as jsonFile:
        json.dump(data, jsonFile)
    return ss
def deleteaccount(userid,opt):
    f = open(f'users/{userid}.json')
    data = json.load(f)
    freeid = data['D_Free_Id']
    freekey = data["D_Free_key"]
    earnid = data['D_Earn_Id']
    earnkey = data['D_Earn_key']
    ref = data['Ref']

    if opt == "earn":
        if "Singapore" in earnkey:
            client = OutlineVPN(api_url=server.sg,
                cert_sha256=server.sg_token)
            client.delete_key(int(earnid))

        elif "Taiwan" in earnkey:
            client = OutlineVPN(api_url=server.sg,
                cert_sha256=server.sg_token)
            client.delete_key(int(earnid))
        else:
            client = OutlineVPN(api_url=server.sg,
                cert_sha256=server.sg_token)
            client.delete_key(int(earnid))


    elif opt == "free":
        if "Singapore" in freekey:
            client = OutlineVPN(api_url=server.sg,
                cert_sha256=server.sg_token)
            client.delete_key(int(freeid))

        elif "Taiwan" in freekey:
            client = OutlineVPN(api_url=server.sg,
                cert_sha256=server.sg_token)
            client.delete_key(int(freeid))
        else:
            client = OutlineVPN(api_url=server.sg,
                cert_sha256=server.sg_token)
            client.delete_key(int(freeid))
    
    