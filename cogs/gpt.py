import discord
from discord.ext import commands
from discord import app_commands
from cogs.tool import generate_card, gpt_answer

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

# 定義名為 Main 的 Cog
class gpt(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        
    # name指令顯示名稱，description指令顯示敘述
    # name的名稱，中、英文皆可，但不能使用大寫英文
    @app_commands.command(name = "塔羅占卜", description = "輸入範例:隆隆今天會出現嗎")
    async def talo(self, interaction: discord.Interaction, quote:str):
        question = "詢問:"+ quote + "，使用塔羅牌解釋抽到:" + generate_card()
        await interaction.response.defer()
        answer = gpt_answer(question)
        await interaction.followup.send(f"根據你的問題:{quote}，以下是我的回答是:\n{answer}")

    @app_commands.command(name = "老鼠聊天", description = "輸入範例:你是誰?")
    async def chat(sef, interaction: discord.Interaction, quote:str):
        await interaction.response.defer()
        answer = gpt_answer(quote)
        await interaction.followup.send(f"根據你的問題:{quote}，以下是我的回答是:\n{answer}")


    
# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(gpt(bot))