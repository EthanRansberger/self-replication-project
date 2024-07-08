import sqlite3
import os

def read_sqlite_files(folder_path):
    """
    Read all SQLite files in the specified folder and extract text from any available columns in the tables.
    
    Args:
        folder_path (str): The path to the folder containing SQLite files.
        
    Returns:
        List[str]: A list of text entries extracted from the SQLite files.
    """
    sqlite_texts = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.sqlite') or filename.endswith('.db'):
            file_path = os.path.join(folder_path, filename)
            if not os.path.exists(file_path):
                print(f"The file {file_path} does not exist.")
                continue

            try:
                conn = sqlite3.connect(file_path)
                cursor = conn.cursor()

                # Get the names of all tables in the database
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()

                if not tables:
                    print(f"No tables found in file {file_path}.")
                    conn.close()
                    continue

                # Extract text from all tables
                for (table_name,) in tables:
                    try:
                        cursor.execute(f"PRAGMA table_info({table_name});")
                        columns_info = cursor.fetchall()
                        columns = [col[1] for col in columns_info]  # Get the column names

                        # Extract text from all columns
                        for column in columns:
                            cursor.execute(f"SELECT {column} FROM {table_name} WHERE {column} IS NOT NULL;")
                            rows = cursor.fetchall()
                            sqlite_texts.extend(str(row[0]) for row in rows if row[0])  # Convert to string and ensure no empty texts

                    except Exception as e:
                        print(f"An error occurred while processing table '{table_name}' in file {file_path}: {e}")

                conn.close()
            except Exception as e:
                print(f"An error occurred while processing file {file_path}: {e}")

    return sqlite_texts
