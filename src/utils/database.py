import sqlite3

class MyDatabase:
    def __init__(self, db_file):
        """
        Initialize a connection to the SQLite3 database.

        Args:
            db_file (str): The name of the database file.
        """
        self.db_file = db_file

    def create_table(self, table_name, data):
        """
        Create a table in the database.

        Args:
            table_name (str): The name of the table to create.
            schema (str): The schema definition of the table (columns and data types).
        """
        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()
            schema = ', '.join([f'{column_name} {column_options}' for column_name, column_options in data.items()])
            cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({schema}')
            conn.commit()
        except sqlite3.Error as e:
            print("SQLite error:", e)
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
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()
            placeholders = ', '.join(['?'] * len(data_list[0]))
            query = f'INSERT INTO {table_name} VALUES ({placeholders})'
            cur.executemany(query, data_list)
            conn.commit()
        except sqlite3.Error as e:
            print("SQLite error:", e)
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
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()
            if fields:
                field_list = ', '.join(fields)
                cur.execute(f'SELECT {field_list} FROM {table_name}')
            else:
                cur.execute(f'SELECT * FROM {table_name}')
            data = cur.fetchall()
            return data
        except sqlite3.Error as e:
            print("SQLite error:", e)
            return None
        finally:
            conn.close()