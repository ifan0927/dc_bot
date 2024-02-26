import re 
import requests
import random
from discord.ext import commands
from openai import OpenAI
import os 

gpt_api_key = os.environ['Gpt_API']

#emoji.py 檢查輸入是否有emoji
def check_emoji(text):
    pattern = r"<a?:\w*:\w*>"
    if re.search(pattern, text):
        return True
    else:
        return False

##emoji.py 下載表情 參數:純表情id,下載路徑
def download_emoji(mode ,emoji_id, save_path):
    try:
        url = "https://cdn.discordapp.com/emojis/"
        if mode == 1:
            link = url + emoji_id + ".png"
        else:
            link = url + emoji_id + ".gif"
        response = requests.get(link)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
                return "下載成功"
        else:
            res = "下載失敗、error code:" + str(response.status_code)
            return res
    except Exception as e:
        return "下載失敗，發生異常：" + str(e)

##emoji.py 將<a:example:1234567>轉換成純id
def get_emoji_id(quote):
    r = []
    if quote[1] == "a":
        r.append(0)
    else:
        r.append(1)
    count = 0
    s = []
    for c in quote:
        if c == ":":
            count += 1
        if c == ">":
            count = 0
        if c != ":" and count == 2:
            s.append(c)
    r.append(''.join(s))
    return r

###gpt.py 產生特定塔羅牌
def generate_card():
    minor_pre = random.choice(['權杖', '寶劍', '聖杯', '錢幣'])
    minor_in = random.choice(['王牌', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '侍者', '騎士', '皇后', '國王'])
    minor_suf = random.choice(['+','-'])
    return minor_pre + minor_in + minor_suf 

###gpt.py 呼叫GPT API 以promt為輸入
def gpt_answer(promt):
    client = OpenAI(
        api_key=gpt_api_key
    )
    completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": promt,
        }
    ],
    temperature=1,
    max_tokens=1000,
    model="gpt-3.5-turbo",
    )
    return completion.choices[0].message.content

async def setup(bot: commands.Bot):
    pass