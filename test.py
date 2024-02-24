import os
from openai import OpenAI
import random


def generate_card():
    minor_pre = random.choice(['權杖', '寶劍', '聖杯', '錢幣'])
    minor_in = random.choice(['王牌', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '侍者', '騎士', '皇后', '國王'])
    minor_suf = random.choice(['+','-'])
    return minor_pre + minor_in + minor_suf 

def gpt_answer(promt):
    client = OpenAI(
        api_key="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"
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
quote = '隆隆今天會出現嗎'
question = "詢問:"+ quote + "，使用塔羅牌解釋抽到:" + generate_card()

print(question)
print(gpt_answer(question))
