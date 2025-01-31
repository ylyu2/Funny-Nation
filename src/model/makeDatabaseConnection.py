import pymysql
import os
import configparser
from loguru import logger
from src.utils.readConfig import getMajorConfig

from pymysql import Connection
from pymysql.cursors import Cursor
from src.utils.readConfig import getMajorConfig

config = getMajorConfig()



def makeDatabaseConnection():
    """
    After you use the connection that returned, make sure that you close it.
    db.close()
    :return: pymysql connect instance
    """
    config = getMajorConfig()
    try:
        db: Connection = pymysql.connect(
            host=config['database']['address'],
            user=config['database']['username'],
            passwd=config['database']['password'],
            database=config['database']['database']
        )
    except Exception as err:
        logger.error(err)
        return None
    return db

