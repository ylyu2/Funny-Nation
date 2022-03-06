from discord import Client, Message
from src.utils.readConfig import getLanguageConfig
import embedLib.help.anonymityBoard as help
languageConfig = getLanguageConfig()

async def getHelpForAnnomity(self: Client, message: Message):
    """
    send help message about Annomity wall
    :param self:
    :param message:
    :return:
    """
    embed = help.getEmbed()
    await message.channel.send(embed=embed)