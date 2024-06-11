import json
import requests
#import servers as server

def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False

def totalusers():
    counts = open(f'usercount.json')
    users = json.load(counts)
    TotalUsers = users['TotalUsers']
    return TotalUsers

def ref(userid):
    f = open(f'users/{userid}.json')
    data = json.load(f)
    pre = data['Ref']
    return pre
def showkeys(userid):
    f = open(f'users/{userid}.json')
    data = json.load(f)
    f = data['D_Free_key']
    e = data['D_Earn_key']

    return f,e

def Dfreekey(userid):
    f = open(f'users/{userid}.json')
    data = json.load(f)
    pre = data['D_Free_key']
    return pre
def Dfreedate(userid):
    f = open(f'users/{userid}.json')
    data = json.load(f)
    pre = data['D_Free_Date']
    return pre
def Dearndate(userid):
    f = open(f'users/{userid}.json')
    data = json.load(f)
    pre = data['D_Earn_Date']
    return pre
def refearn(userid):
    f = open(f'users/{userid}.json')
    data = json.load(f)
    pre = data['Ref']
    post = pre + 500 # to change Referral Dat                    
    if post < 50000:                   
        data["Ref"] = post
        with open(f'users/{userid}.json', "w") as jsonFile:
            json.dump(data, jsonFile)
def adduser(userid):
    default_data = {
                "Ref": 500,
                "D_Free_key": "0",
                "D_Free_Date": "0",
                "D_Free_Id":3,
                "D_Earn_key": "0",
                "D_Earn_Date": "0",
                "D_Earn_Id":3,
                "Role": "N"
            }
    with open(f"users/{userid}.json", "w") as outfile:
                json.dump(default_data, outfile)


     
     