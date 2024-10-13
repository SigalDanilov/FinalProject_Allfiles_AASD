import mysql.connector

# Step 1: Connect to MySQL database
# Establish a connection to the MySQL database using the specified credentials (host, user, password, database).
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'fp_db'  # The name of your database
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Step 2: SQL query to delete all rows where class = 0
# This query deletes all rows from the 'posts_new' table where the 'class' column has a value of 0.
delete_query = "DELETE FROM posts_new WHERE class = 0"

# Step 3: Execute the deletion query
# Execute the SQL query that removes all records with class = 0.
cursor.execute(delete_query)

# Step 4: Commit the changes to the database
# Apply the changes to the database (i.e., save the deletion action).
conn.commit()

# Step 5: Close the cursor and connection
# Close the cursor and database connection to free up resources after the deletion is done.
cursor.close()
conn.close()

print("Rows with class = 0 have been deleted.")
