import json

from loguru import logger
from datetime import datetime
import uuid
from pymysql import Connection
from pymysql.cursors import Cursor
from typing import List

def newAward(db: Connection, senderID: int, messageID: int, money: int, eventName: str) -> bool:
    if db is None:
        return False

    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"INSERT INTO `eventAward` (`eventManagerID`, `eventMsgID`, `money`, `eventName`, `status`) VALUES ({senderID}, {messageID}, {money}, '{eventName}', 0);")
        db.commit()

    except Exception as err:
        logger.error(err)
        return False
    return True


def deletAward(db: Connection,  messageID: int) -> bool:
    if db is None:
        return False
    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"DELETE FROM `eventAward` WHERE `eventMsgID` = '{messageID}';")
        db.commit()
    except Exception as err:
        logger.error(err)
        return False
    return True

def getEventAwardByName(db: Connection,  eventName: str):
    if db is None:
        return None
    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `eventAward` WHERE `eventName` = '{eventName}' AND `status` = 0;")
        result: tuple = cursor.fetchone()
    except Exception as err:
        logger.error(err)
        return None
    return result

def getEventAward(db: Connection, messageID: int) ->tuple or None:
    if db is None:
        return None
    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `eventAward` WHERE `eventMsgID` = '{messageID}';")
        result: tuple = cursor.fetchone()
    except Exception as err:
        logger.error(err)
        return None
    return result

def addRecipient(db: Connection, messageID: int, approvePrivateMSGID: int, recipientID: int) -> bool:
    if db is None:
        return False

    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"INSERT INTO `eventAwardRecipients` (`eventMsgID`, `recipientID`, `approvePrivateMSGID`, `status`) VALUES ({messageID}, {recipientID}, {approvePrivateMSGID}, 0);")
        db.commit()

    except Exception as err:
        logger.error(err)
        return False
    return True

def removeRecipient(db: Connection, messageID: int) -> bool:
    if db is None:
        return False
    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"DELETE FROM `eventAwardRecipients` WHERE `eventMsgID` = '{messageID}';")
        db.commit()
    except Exception as err:
        logger.error(err)
        return False
    return True

def searchRecipientsByPrivateMSGID(db: Connection, approvePrivateMSGID: int) -> tuple or None:
    if db is None:
        return None
    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `eventAwardRecipients` WHERE `approvePrivateMSGID` = {approvePrivateMSGID};")
        result: tuple = cursor.fetchone()
    except Exception as err:
        logger.error(err)
        return None
    return result

def approveRecipients(db: Connection, approvePrivateMSGID: int) -> bool:
    if db is None:
        return False
    try:
        cursor: Cursor = db.cursor()
        sql = f"UPDATE `eventAwardRecipients` SET  `status` = 2 WHERE `eventAwardRecipients` . `approvePrivateMSGID` = '{approvePrivateMSGID}';"
        cursor.execute(sql)
        db.commit()
    except Exception as err:
        logger.error(err)
        return False
    return True

def rejectRecipients(db: Connection, approvePrivateMSGID: int) -> bool:
    if db is None:
        return False
    try:
        cursor: Cursor = db.cursor()
        sql = f"UPDATE `eventAwardRecipients` SET  `status` = 1 WHERE `eventAwardRecipients` . `approvePrivateMSGID` = '{approvePrivateMSGID}';"
        cursor.execute(sql)
        db.commit()
    except Exception as err:
        logger.error(err)
        return False
    return True

def searchRecipientByEventIDandRecipientID(db: Connection, eventMSGID: int, recipientID: int) -> tuple or None:
    if db is None:
        return None
    try:
        cursor: Cursor = db.cursor()
        cursor.execute(f"SELECT * FROM `eventAwardRecipients` WHERE `eventMsgID` = {eventMSGID} AND `recipientID` = {recipientID};")
        result: tuple = cursor.fetchone()
    except Exception as err:
        logger.error(err)
        return None
    return result

def closeEvent(db: Connection, messageID: int) -> bool:
    if db is None:
        return False
    try:
        cursor: Cursor = db.cursor()
        sql = f"UPDATE `eventAward` SET  `status` = 1 WHERE `eventAward` . `eventMsgID` = '{messageID}';"
        cursor.execute(sql)
        db.commit()
    except Exception as err:
        logger.error(err)
        return False
    return True



