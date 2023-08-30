import os

db_filename = "database/flowers.db"

if os.path.exists(db_filename):
    print("Database file exists.")
else:
    print("Database file does not exist. You might need to create it first.")

