import os
import sqlite3

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Calculate the script directory (python_files)
script_dir = os.path.dirname(script_path)

# Calculate the project directory (project_sqlite)
project_dir = os.path.abspath(os.path.join(script_dir, ".."))

# Calculate the database directory
database_dir = os.path.join(project_dir, "database")

# Create the 'database' directory if it doesn't exist
if not os.path.exists(database_dir):
    os.makedirs(database_dir)

# Calculate the database file path
db_path = os.path.join(database_dir, "flowers.db")

# Create the database file
conn = sqlite3.connect(db_path)
conn.close()

print(f"Empty database file 'flowers.db' created at '{os.path.basename(db_path)}'")


# import os
# import sqlite3

# # Set the path to the 'database' directory within the project
# database_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "database"))

# # Create the 'database' directory if it doesn't exist
# if not os.path.exists(database_dir):
#     os.makedirs(database_dir)

# # Set the path to the 'flowers.db' database file
# db_path = os.path.join(database_dir, 'flowers.db')

# # Create the database file
# conn = sqlite3.connect(db_path)
# conn.close()

# # print(f"Empty database file 'flowers.db' created at '{db_path}'")
# print(f"Empty database file 'flowers.db' created at '{os.path.basename(db_path)}'")

