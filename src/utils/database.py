import sqlite3
from src.utils.logs_manager import logger

class MyDatabase:
    def __init__(self, db_file):
        """
        Initialize a connection to the SQLite3 database.

        Args:
            db_file (str): The name of the database file.
        """
        self.db_file = db_file
        logger.info(f"la base données {db_file} a été chargée avec succès")

    def create_table(self, table_name, data):
        """
        Create a table in the database.

        Args:
            table_name (str): The name of the table to create.
            schema (str): The schema definition of the table (columns and data types).
        """
        try:
            conn, cur = self.connect()
            schema = ', '.join([f'{column_name} {column_options}' for column_name, column_options in data.items()])
            logger.info(f"création de la table {table_name} avec comme champs {schema}")
            cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({schema})')
            logger.info(f"création de la table {table_name} réussi")
            conn.commit()
        except sqlite3.Error as e:
            logger.error(e)
        finally:
            conn.close()

    def insert_data(self, table_name, data_list):
        """
        Insert data into a table in the database.

        Args:
            table_name (str): The name of the table to insert data into.
            data_list (list): A list of tuples, where each tuple represents a row of data to insert.
        """
        try:
            conn, cur = self.connect()
            placeholders = ', '.join(['?'] * len(data_list[0]))
            logger.info(f"insertion de {data_list}")
            query = f'INSERT INTO {table_name} VALUES ({placeholders})'
            cur.executemany(query, data_list)
            logger.info(f"insertion de {data_list} réussi")
            conn.commit()
        except sqlite3.Error as e:
            logger.error(e)
        finally:
            conn.close()

    def get_data(self, table_name, fields=None):
        """
        Retrieve data from a table.

        Args:
            table_name (str): The name of the table to retrieve data from.
            fields (list): A list of field names to retrieve. If None, all fields are retrieved.

        Returns:
            list: A list of tuples, where each tuple represents a row of data.
        """
        try:
            conn, cur = self.connect()
            if fields:
                field_list = ', '.join(fields)
                cur.execute(f'SELECT {field_list} FROM {table_name}')
            else:
                cur.execute(f'SELECT * FROM {table_name}')
            data = cur.fetchall()
        except sqlite3.Error as e:
            logger.error(e)
        finally:
            conn.close()
            logger.info(data)
            return data
    
    def connect(self):
        conn = sqlite3.connect(self.db_file)
        logger.info(f"connection a la db {self.db_file}")
        cur = conn.cursor()
        return conn, cur