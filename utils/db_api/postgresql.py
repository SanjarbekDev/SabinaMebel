from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
              user=config.DATABASE_URL,
#             password=config.DB_PASS,
#             host=config.DB_HOST,
#             database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture1(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture1 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture2(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture2 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture3(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture3 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture4(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture4 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture5(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture5 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture6(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture6 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture7(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture7 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture8(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture8 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_capture9(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Capture9 (
        id SERIAL PRIMARY KEY,
        file_id VARCHAR(500) NOT NULL,
        caption varchar(1000) NULL 
        );
        """
        await self.execute(sql, execute=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def add_capture1(self,file_id, caption):
        sql = "INSERT INTO Capture1 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture2(self,file_id, caption):
        sql = "INSERT INTO Capture2 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture3(self,file_id, caption):
        sql = "INSERT INTO Capture3 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture4(self,file_id, caption):
        sql = "INSERT INTO Capture4 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture5(self,file_id, caption):
        sql = "INSERT INTO Capture5 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture6(self,file_id, caption):
        sql = "INSERT INTO Capture6 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture7(self,file_id, caption):
        sql = "INSERT INTO Capture7 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture8(self,file_id, caption):
        sql = "INSERT INTO Capture8 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def add_capture9(self,file_id, caption):
        sql = "INSERT INTO Capture9 (file_id, caption) VALUES($1, $2) returning *"
        return await self.execute(sql, file_id, caption, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_all_capture1(self):
        sql = "SELECT * FROM Capture1"
        return await self.execute(sql, fetch=True)

    async def select_all_capture2(self):
        sql = "SELECT * FROM Capture2"
        return await self.execute(sql, fetch=True)

    async def select_all_capture3(self):
        sql = "SELECT * FROM Capture3"
        return await self.execute(sql, fetch=True)

    async def select_all_capture4(self):
        sql = "SELECT * FROM Capture4"
        return await self.execute(sql, fetch=True)
    
    async def select_all_capture5(self):
        sql = "SELECT * FROM Capture5"
        return await self.execute(sql, fetch=True)

    async def select_all_capture6(self):
        sql = "SELECT * FROM Capture6"
        return await self.execute(sql, fetch=True)

    async def select_all_capture7(self):
        sql = "SELECT * FROM Capture7"
        return await self.execute(sql, fetch=True)

    async def select_all_capture8(self):
        sql = "SELECT * FROM Capture8"
        return await self.execute(sql, fetch=True)

    async def select_all_capture9(self):
        sql = "SELECT * FROM Capture9"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    async def drop_capture1(self):
        await self.execute("DROP TABLE Capture1", execute=True)

    async def drop_capture2(self):
        await self.execute("DROP TABLE Capture2", execute=True)

    async def drop_capture3(self):
        await self.execute("DROP TABLE Capture3", execute=True)

    async def drop_capture4(self):
        await self.execute("DROP TABLE Capture4", execute=True)

    async def drop_capture5(self):
        await self.execute("DROP TABLE Capture5", execute=True)

    async def drop_capture6(self):
        await self.execute("DROP TABLE Capture6", execute=True)

    async def drop_capture7(self):
        await self.execute("DROP TABLE Capture7", execute=True)

    async def drop_capture8(self):
        await self.execute("DROP TABLE Capture8", execute=True)

    async def drop_capture9(self):
        await self.execute("DROP TABLE Capture9", execute=True)
