import sqlite3
import os

# Set the path to the project directory
project_dir = os.path.dirname(os.getcwd())

# Set the path to the 'database' directory within the project
database_dir = os.path.join(project_dir, 'database')

# Set the path to the 'flowerss.db' database file
db_path = os.path.join(database_dir, 'flowers.db')

# Connect to the 'flowers.db' database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create Flowers table
cursor.execute('''
    CREATE TABLE Flowers (
        FlowerID INT PRIMARY KEY,
        CommonName VARCHAR(255),
        ScientificName VARCHAR(255),
        Family VARCHAR(255),
        Color VARCHAR(50),
        BloomSeason VARCHAR(50)
    )
''')

# Create Locations table
cursor.execute('''
    CREATE TABLE Locations (
        LocationID INT PRIMARY KEY,
        LocationName VARCHAR(255),
        City VARCHAR(100),
        Country VARCHAR(100),
        Climate VARCHAR(100),
        Altitude INT
    )
''')

# Create CareGuides table
cursor.execute('''
    CREATE TABLE CareGuides (
        GuideID INT PRIMARY KEY,
        FlowerID INT,
        LightRequirements VARCHAR(255),
        WateringSchedule VARCHAR(255),
        SoilType VARCHAR(100),
        PruningInfo VARCHAR(255),
        FOREIGN KEY (FlowerID) REFERENCES Flowers(FlowerID)
    )
''')

# Create Purchases table
cursor.execute('''
    CREATE TABLE Purchases (
        PurchaseID INT PRIMARY KEY,
        FlowerID INT,
        LocationID INT,
        PurchaseDate DATE,
        Quantity INT,
        TotalCost DECIMAL(10, 2),
        FOREIGN KEY (FlowerID) REFERENCES Flowers(FlowerID),
        FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
    )
''')

# Commit and close the connection
conn.commit()
conn.close()

print(f"Tables created in the 'flowerss.db' database")
