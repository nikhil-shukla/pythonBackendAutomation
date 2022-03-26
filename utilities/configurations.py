import configparser

import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('F://Udemy//pythonProject//BackendAutomation//utilities//properties.ini')
    return config


dbConnect_config = {
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password']
}


def getPwd():
    return 'github147'


def getAccessToken():
    return {"Authorization": "Bearer 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"}


def open_dbConnection():
    try:
        conn = mysql.connector.connect(**dbConnect_config)
        if conn.is_connected():
            print('Connection Successful')
            return conn
    except Error as e:
        print(e)


def close_dbConnection():
    conn = open_dbConnection()
    try:
        conn.close()
        if conn.is_closed():
            print('Connection is closed')
    except Error as e:
        print(e)


def getQuery(query):
    conn = open_dbConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
