import logging
import os
import datetime
import json
from datetime import timedelta
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.deep_linking import get_start_link
from aiogram.utils.deep_linking import decode_payload
from plugins.utlis import check_sub,totalusers,refearn,adduser,ref,Dfreedate
from plugins.generateCF import cf_crawl
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6076763989:AAEw6e6E3wff3L7iBRlA5HDoOuMnVBi-cWE' # MODSBOTS_BOT
CHANNEL_ID = '@modsbots_tech'
NOT_SUB = 'ကျနော်တို့ ချန်နယ် လေးကို အရင် Subscribe လုပ်ပေးပါ'
ANOTHER_NOT_SUB = 'ချန်နယ်ကို Subscribe လုပ်ထားခြင်းမရှိပါ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
def keyboard(user_id):
    StartKeyboard = ReplyKeyboardMarkup(resize_keyboard = True).add('>>>GENERATE VPN CONFIG<<<')
    return StartKeyboard

@dp.message_handler(commands=['start']) 
async def start(message: types.Message):    
    if message.chat.type == 'private':
            args = message.get_args()
            payload = decode_payload(args)
            add_user = (totalusers()) + 1
            user_id=message.from_user.id
            if not os.path.exists(f"users/{user_id}.json"): 
                adduser(user_id)             
                if not payload == "":
                    refearn(payload)
                else:
                    pass
                f = open('usercount.json')
                data = json.load(f)
                data['TotalUsers'] = add_user
                with open('usercount.json', "w") as jsonFile:
                    json.dump(data, jsonFile)
                await bot.send_message(message.from_user.id, f'ကျနော် တို့ အခမဲ့ CloudFlare VPN Bot လေးကနေ ကြိုဆိုလိုက်ပါတယ်', reply_markup=keyboard(message.from_user.id))
            else:
                await bot.send_message(message.from_user.id, f'CloudFlare VPN Bot လေးကနေ ပြန်လည် ကြိုဆိုလိုက်ပါတယ်', reply_markup=keyboard(message.from_user.id))

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        #if user will try to write 'Profile' without subscription
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            if message.text == '>>>GENERATE VPN CONFIG<<<':
                await bot.send_message(message.from_user.id,'🚀.......ခနစောင့်ပါ.......🚀', reply_markup=keyboard(message.from_user.id))
                vless =  cf_crawl()
                if not vless == "":
                    await bot.send_message(message.from_user.id,vless, reply_markup=keyboard(message.from_user.id))
                else:
                    await bot.send_message(message.from_user.id,'ထပ်မံကြိုးစားကြည့်ပါ', reply_markup=keyboard(message.from_user.id))
            
               
        else:
            await bot.send_message(message.from_user.id, 'ကျွန်တော်တို့ ချန်နယ်လေးကို SUBSCRIBE ထားသူများသာ အသုံးပြုနိုင်ပါသည် @binbeginner ကိုအရင် SUBSCRIBE လုပ်ပါ',reply_markup=keyboard(message.from_user.id))      
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
