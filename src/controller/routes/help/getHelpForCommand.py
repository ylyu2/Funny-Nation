from discord import Client, Message
from src.utils.readConfig import getLanguageConfig
from src.utils.readConfig import getGeneralConfig
import embedLib.help.commands as help
languageConfig = getLanguageConfig()
generalConfig = getGeneralConfig()
async def getHelpForCommand(self: Client, message: Message):
    """
    send help message about all commands bot provided
    :param self:
    :param message:
    :return:
    """
    prefix = generalConfig['command']['prefix']
    embed = help.getEmbed(prefix)
    await message.channel.send(embed=embed)