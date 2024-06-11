from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

policy = InlineKeyboardButton(text='စည်းကမ်းချက်များကိုဖတ်မည်', callback_data='policy')

def servermenus(sv):
    SSHServersMenu = InlineKeyboardMarkup(row_width=3)
    sg = InlineKeyboardButton(text='စင်ကာပူ', callback_data=f'{sv}_sg_server')
    tw = InlineKeyboardButton(text='ထိုင်ဝမ်', callback_data=f'{sv}tw_server')
    jp =  InlineKeyboardButton(text='ဂျပန်', callback_data=f'{sv}_jp_server')
    us =  InlineKeyboardButton(text='အမေရိကန်', callback_data=f'{sv}_us_server')
    kr =  InlineKeyboardButton(text='ကိုရီးယား', callback_data=f'{sv}_kr_server')

    SSHServersMenu.insert(sg)
    SSHServersMenu.insert(tw)
    SSHServersMenu.insert(jp)
    SSHServersMenu.insert(us)
    SSHServersMenu.insert(kr)

    return SSHServersMenu

def optionmenu(proto):
    Menu = InlineKeyboardMarkup(row_width=3)
    a = InlineKeyboardButton(text='အခမဲ့ကီး', callback_data=f'{proto}_server_create_free_key')
    b = InlineKeyboardButton(text='3GB ထုတ်ယူမည်', callback_data=f'{proto}_server_create_earn_key')
    c =  InlineKeyboardButton(text='ကျွန်ုပ်၏ကီး', callback_data=f'show_my_key')
    policy = InlineKeyboardButton(text='စည်းကမ်းချက်များကိုဖတ်မည်', callback_data='policy')
    Menu.insert(a)
    Menu.insert(b)
    Menu.insert(c)
    Menu.insert(policy)
    return Menu

def gcp_atom(proto):
    Menu = InlineKeyboardMarkup(row_width=2)
    a = InlineKeyboardButton(text='GCP-VMESS', callback_data=f'{proto}_gcp')
    b = InlineKeyboardButton(text='ATOM-VMESS', callback_data=f'{proto}_atom')
    policy = InlineKeyboardButton(text='စည်းကမ်းချက်များကိုဖတ်မည်', callback_data='policy')
    Menu.insert(a)
    Menu.insert(b)
    Menu.insert(policy)
    return Menu
def policymenu():
    PolicyMenu = InlineKeyboardMarkup(row_width=1)
    policy = InlineKeyboardButton(text='စည်းကမ်းချက်များကိုဖတ်မည်', callback_data='policy')
    PolicyMenu.insert(policy)
    return PolicyMenu

APKUrl = InlineKeyboardButton(text='Android', url='https://play.google.com/store/apps/details?id=com.napsternetlabs.napsternetv&hl=en&gl=US&pli=1')
IOSUrl = InlineKeyboardButton(text='Apple Ios', url='https://apps.apple.com/us/app/napsternetv/id1629465476')
policy = InlineKeyboardButton(text='စည်းကမ်းချက်များကိုဖတ်မည်', callback_data='policy')
DEVICEMenu = InlineKeyboardMarkup(row_width=2)

DEVICEMenu.insert(APKUrl)
DEVICEMenu.insert(IOSUrl)
DEVICEMenu.insert(policy)

freeMenu = InlineKeyboardMarkup(row_width=1)
freebtn =  InlineKeyboardButton(text='အခမဲ့ကီး', callback_data='#')
freeMenu.insert(freebtn)

earnMenu = InlineKeyboardMarkup(row_width=1)
earnbtn =  InlineKeyboardButton(text='လဲလှယ်ထားသည့်ကီး', callback_data='#')
earnMenu.insert(earnbtn)