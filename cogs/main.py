import discord
from discord.ext import commands
global py_switch
py_switch = 1
# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        global py_switch
        if message.author == self.bot.user:
            return
        if message.content == "開關屁眼":
            if py_switch == 1: 
                py_switch = 0
                await message.channel.send("PY關閉")
            else: 
                py_switch = 1
                await message.channel.send("PY開啟")
            
        if "py"  in message.content.lower() and py_switch == 1 :
            await message.channel.send("<a:ezgif:1207301388732727326>")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))
