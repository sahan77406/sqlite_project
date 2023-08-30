import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database\my_data_base.db')  # Replace with the actual database name

# Create a cursor to interact with the database
cursor = conn.cursor()

# SQL query
query = """
    SELECT albums.AlbumId, albums.Title, albums.ArtistId
    FROM albums
    JOIN artists ON albums.ArtistId = artists.ArtistId;
"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print("AlbumId:", row[0])
    print("Title:", row[1])
    print("ArtistId:", row[2])
    print("------------")

# Close the cursor and the connection
cursor.close()
conn.close()
