from discord import Client, Message
from src.utils.readConfig import getVipTagsConfig
from src.utils.readConfig import getGeneralConfig
import embedLib.help.howToBuyVIP as help
VIPConfig = getVipTagsConfig()
generalConfig = getGeneralConfig()

async def getHelpForVIP(self: Client, message: Message):
    sections: str = VIPConfig.sections()
    prefix = generalConfig['command']['prefix']
    field = ""
    for i in range(0, len(VIPConfig.sections())):
        vipNnumber: str = sections[i]
        VIPName = VIPConfig[vipNnumber]['name']
        giftMoney = int(VIPConfig[vipNnumber]['price']) / 100
        field += f"{VIPName}-{giftMoney}\n"
    embed = help.getEmbed(field, prefix)
    await message.channel.send(embed=embed)

