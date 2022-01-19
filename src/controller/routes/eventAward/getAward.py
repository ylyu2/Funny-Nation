import json
from typing import List
from discord import Client, TextChannel, Guild, Member, Message
from pymysql import Connection
import src.model.eventAwardManagement as eventAwardManagement
from src.model.userManagement import getUser, addMoneyToUser
from src.model.cashFlowManagement import addNewCashFlow
from src.utils.readConfig import getLanguageConfig, getMajorConfig
from src.controller.routes.eventAward.adminProof import adminProof

def getAward(self: Client, messageID: int, db: Connection, channelID: int, userID: int, eventAdmin: list):
    languageConfig = getLanguageConfig()
    majorConfig = getMajorConfig()

    myGuild: Guild = self.guilds[0]
    user: Member = await myGuild.fetch_member(userID)
    channels: List[TextChannel] = myGuild.text_channels
    targetChannel: TextChannel or None = None
    for channel in channels:
        if channel.id == channelID:
            targetChannel = channel
            break

    AwardInfo = eventAwardManagement.getEventAward(db, messageID)
    invove: dict = json.loads(AwardInfo[4])

    moneyAward = eventAwardManagement[3]
    dbresult = True
    dbresult = dbresult and eventAwardManagement.takeAward(db, messageID,moneyAward)
    dbresult = dbresult and addMoneyToUser(db, userID, moneyAward)
    dbresult = dbresult and addNewCashFlow(db, userID, moneyAward, majorConfig['cashFlowMessage']['getAward'])
    dbresult = dbresult and eventAwardManagement.editRecipient(db, messageID, json.dumps(invove))

    await targetChannel.send("you got it")
    await adminProof(self, db, AwardInfo[4])

