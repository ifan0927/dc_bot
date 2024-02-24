import discord
import pygsheets
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
gc = pygsheets.authorize(service_file='google_key.json')
sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1UoFvx8QVt3tMS2aIcPVbsDXzTjbp6uuUvzqNjFV5ySE/edit#gid=300248812')


def get_mit(sheet,mech):
    wks = sht[sheet]
    mit = []
    for column in range(19):
        if wks.cell(chr(66+column)+str(mech)).value != "FALSE":
            mit.append(wks.cell(chr(66+column) + "1").value)

    return mit

# 定義名為 ffxiv_raid 的 Cog
class ffxiv_raid(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "dsr-p6":
            await message.channel.send(sht[6].cell("B1").value)
        
    @app_commands.command(name = "dsr-p6減傷", description = "選擇特定機制")
    @app_commands.describe(mech = "選擇機制")
    @app_commands.choices(
        mech = [
            Choice(name = "塔分攤1", value = 2),
            Choice(name = "隕石1", value = 3),
            Choice(name = "塔分攤2", value = 4),
            Choice(name = "隕石2", value = 5),
            Choice(name = "塔分攤3", value = 6)
        ]
    )
    async def order(self, interaction: discord.Interaction, mech: Choice[int]):
        await interaction.response.defer()
        sheet = 6
        mit = get_mit(sheet,mech.value)
        await interaction.followup.send(mit)

    

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(ffxiv_raid(bot))