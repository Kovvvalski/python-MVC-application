from dbconnection.dbproperties import *
from exception.dbexception import DBException
from log.my_logger import logger
import atexit
import mysql.connector


def close_connection() -> None:
    try:
        connection.close()
    except Exception as e:
        logger.error('Can not create connection')
        raise DBException('Can not create connection', err)
    logger.info('Connection closed')


connection = None

try:
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    connection.autocommit = True
except mysql.connector.Error as err:
    logger.fatal("Can not create connection")
    raise DBException("Can not create connection", err)

logger.info("Connection was successfully created")
atexit.register(close_connection)
