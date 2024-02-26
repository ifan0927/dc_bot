import discord
from discord.ext import commands
from discord import app_commands
from cogs.tool import check_emoji, get_emoji_id,download_emoji
import asyncio

# 定義名為 Main 的 Cog
class emoji(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        '''
        if message.content == "guild":
            await message.channel.send(message.guild.name)
        
        if check_emoji(message.content) :
            emoji_id =  get_emoji_id(message.content)
            await message.channel.send(emoji_id)
        '''

    @app_commands.command(name = "表情", description = "輸入一個表情")
    @app_commands.describe(emoji = "輸入一個表情", emoji_name = "表情在伺服器的名稱")
    async def emoji_input(sef, interaction: discord.Interaction, emoji:str, emoji_name:str):
        #檢查是否為emoji
        if check_emoji(emoji):
            #get_emoji_id()傳回list[0]- 0為動圖 1為png list[1]為id 
            emoji_id =  get_emoji_id(emoji)
            name = "emoji.png"
            await interaction.response.defer()
            await asyncio.to_thread(download_emoji, emoji_id[0], emoji_id[1], name)
            try:
                with open('emoji.png', 'rb') as f:
                    data = f.read()
                    status = await interaction.guild.create_custom_emoji(name=emoji_name, image=data)
                    if emoji_id[0] == 0 :
                        status = "表情新增成功:" "<a:" + emoji_name + ":" + str(status.id) + ">"
                    else:
                        status = "表情新增成功:" "<:" + emoji_name + ":" + str(status.id) + ">"
                #.guild.create_custom_emoji("test", "emoji.png",)
            except Exception as e:
                status = f"新增失敗、error:{e}" 
            
            await interaction.followup.send(status)
        else:
            await interaction.response.defer()
            await interaction.followup.send(f"{interaction.user.mention} 叫你第一個輸入表情，不懂是不是，傻逼 <:xddfuck:1189041718104956989>")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(emoji(bot))