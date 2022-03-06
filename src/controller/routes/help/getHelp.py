
from discord import Client, Message, Guild, Member
from src.utils.readConfig import getLanguageConfig
import embedLib.help.getHelp as help
languageConfig = getLanguageConfig()

async def getHelp(self: Client, message: Message):
    """
    send help message about how to play BlackJack by bot
    :param self:
    :param message:
    :return:
    """
    embed = help.getEmbed()
    await message.channel.send(embed=embed)
