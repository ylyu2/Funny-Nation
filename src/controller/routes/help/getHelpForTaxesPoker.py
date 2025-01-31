from discord import Client, Message
from src.utils.readConfig import getLanguageConfig
from src.utils.readConfig import getGeneralConfig
import embedLib.help.holdem as help
languageConfig = getLanguageConfig()
generalConfig = getGeneralConfig()

async def getHelpForTaxesPoker(self: Client, message: Message):
    prefix = generalConfig['command']['prefix']
    embed = help.getEmbed(prefix)
    await message.channel.send(embed=embed)