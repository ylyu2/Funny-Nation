from discord import Client, Message, Guild, Member
from src.utils.readConfig import getLanguageConfig
import embedLib.help.howToGetMoney as help
languageConfig = getLanguageConfig()


async def getHelpForMoney(self: Client, message: Message):
    """
    send help message about money system
    :param self:
    :param message:
    :return:
    """
    embed = help.getEmbed()
    await message.channel.send(embed=embed)