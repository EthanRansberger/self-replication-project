import os
import sqlite3

def initialize_database(db_path, sqlite_folder_path):
    """
    Initialize the SQLite database and copy data from all .sqlite files in the given folder path.
    """
    # Connect to the main database (will create it if it doesn't exist)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # Walk through all files in the given folder path
        for root, dirs, files in os.walk(sqlite_folder_path):
            for file in files:
                if file.endswith('.sqlite'):
                    file_path = os.path.join(root, file)
                    attach_and_copy_data(conn, cursor, file_path)

def attach_and_copy_data(conn, cursor, file_path):
    """
    Attach an SQLite file and copy its data to the main database.
    """
    db_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Attach the database
    cursor.execute(f"ATTACH DATABASE '{file_path}' AS {db_name}")
    
    # Get the list of tables in the attached database
    cursor.execute(f"SELECT name FROM {db_name}.sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Copy each table's data
    for table_name in tables:
        table_name = table_name[0]
        cursor.execute(f"CREATE TABLE IF NOT EXISTS main.{table_name} AS SELECT * FROM {db_name}.{table_name} WHERE 1=0")
        cursor.execute(f"INSERT INTO main.{table_name} SELECT * FROM {db_name}.{table_name}")
    
    # Detach the database
    cursor.execute(f"DETACH DATABASE {db_name}")
    conn.commit()

if __name__ == "__main__":
    db_path = 'C:/Users/Ethan/Documents/sample/database.db'  # Path to your main SQLite database
    sqlite_folder_path = 'C:/Users/Ethan/Documents/sample/sqlite_files/'  # Path to your folder containing SQLite files
    initialize_database(db_path, sqlite_folder_path)
