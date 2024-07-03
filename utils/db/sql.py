import os
import mysql.connector.pooling
import aiomysql
import asyncio

async def build_async_sql_pool():
    return await aiomysql.create_pool(
        # host='localhost',
        # user=os.getenv('SQL_USER_LOCAL'),
        # password=os.getenv('SQL_PASSWORD_LOCAL'),
        # -----------------------------------------
        host="database-v5.cxu0oc6yqrfs.us-east-1.rds.amazonaws.com",
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PASSWORD'),
        # -----------------------------------------
        port=3306,
        db='basic_db',
        minsize=1,
        maxsize=10,
        loop=asyncio.get_event_loop()
    )



def sql_pool_buildup():
    pool_config = {
        'pool_name': 'day_trip_pool',
        'pool_size': 10,
        # -----------------------------------------
        'host':"database-v5.cxu0oc6yqrfs.us-east-1.rds.amazonaws.com",
        'user':os.getenv('SQL_USER'),
        'password':os.getenv('SQL_PASSWORD'),
        # -----------------------------------------
        # 'host': '52.4.229.207',
        # 'user': os.getenv('SQL_USER'),
        # 'password': os.getenv('SQL_PASSWORD'),
        # -----------------------------------------
        # 'host': 'localhost',
        # 'user': os.getenv('SQL_USER_LOCAL'),
        # 'password': os.getenv('SQL_PASSWORD_LOCAL'),
            
        'database': 'basic_db',
        'port': 3306,
        'use_pure': True
    }
    return mysql.connector.pooling.MySQLConnectionPool(**pool_config)