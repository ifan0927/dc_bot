import discord
import os
from openai import OpenAI
from discord.ext import commands
from discord import app_commands
import random

gpt_api_key = os.environ['Gpt_API']

def generate_card():
    minor_pre = random.choice(['權杖', '寶劍', '聖杯', '錢幣'])
    minor_in = random.choice(['王牌', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '侍者', '騎士', '皇后', '國王'])
    minor_suf = random.choice(['+','-'])
    return minor_pre + minor_in + minor_suf 

def gpt_answer(promt):
    client = OpenAI(
        api_key="gpt_api_key"
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

# 定義名為 Main 的 Cog
class gpt(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "給我一張塔羅牌":
            await message.channel.send(generate_card)
        
    # name指令顯示名稱，description指令顯示敘述
    # name的名稱，中、英文皆可，但不能使用大寫英文
    @app_commands.command(name = "塔羅占卜", description = "輸入範例:隆隆今天會出現嗎")
    async def talo(self, interaction: discord.Interaction, quote:str):
        question = "詢問:"+ quote + "，使用塔羅牌解釋抽到:" + generate_card()
        await interaction.response.defer()
        answer = gpt_answer(question)
        await interaction.followup.send(answer)

    @app_commands.command(name = "測試", description = "測試用")
    async def test(interaction: discord.Interaction, quote:str):
        await interaction.response.send_message(quote)


    
# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(gpt(bot))