from discord import Client, Message
from src.utils.readConfig import getLanguageConfig
from src.utils.readConfig import getGiftConfig
from src.utils.readConfig import getGeneralConfig
import embedLib.help.sendGift as help
languageConfig = getLanguageConfig()
giftConfig = getGiftConfig()
generalConfig = getGeneralConfig()
async def getHelpForGift(self: Client, message: Message):
    sections: str = giftConfig.sections()
    generalConfig = getGeneralConfig()
    prefix = generalConfig['command']['prefix']
    description: str = ""

    for i in range(0, len(giftConfig.sections())):
        giftName: str = sections[i]
        giftMoney = int(giftConfig[giftName]['amount']) / 100
        description += f"{giftName}: {giftMoney}元\n"
    embed = help.getEmbed(description, prefix)
    await message.channel.send(embed=embed)