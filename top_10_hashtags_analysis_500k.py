import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to MySQL database
# Establish a connection to the MySQL database using the specified host, user, password, and database.
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='FP_Database'
)

# Step 2: Query data from the Hashtags_In_Posts table (limit to first 500,000 rows)
# SQL query to fetch the first 500,000 rows from the 'Hashtags_In_Posts' table.
hashtags_query = "SELECT * FROM Hashtags_In_Posts LIMIT 500000"

# Step 3: Read the data from the query into a pandas DataFrame
# Execute the query and load the result into a DataFrame for further analysis.
hashtags_df = pd.read_sql(hashtags_query, cnx)

# Step 4: Close the MySQL connection
# Close the connection to the database to free up resources.
cnx.close()

# Step 5: Data Preprocessing - Convert hashtags to lowercase
# Convert all hashtags to lowercase to ensure case-insensitive counting (i.e., 'Hashtag' and 'hashtag' are treated the same).
hashtags_df['hashtag'] = hashtags_df['hashtag'].str.lower()

# Step 6: Count the occurrences of each hashtag
# Count the number of times each hashtag appears in the 'hashtag' column and sort them in descending order.
hashtags_counts = hashtags_df['hashtag'].value_counts()

# Step 7: Select the top 10 most frequently used hashtags
# Extract the top 10 hashtags by selecting the first 10 entries from the sorted counts.
top_hashtags = hashtags_counts.head(10)

# Step 8: Visualization - Create a bar chart of the top 10 most used hashtags
# Plot the top 10 hashtags as a bar chart with the hashtags on the x-axis and their counts on the y-axis.
plt.bar(top_hashtags.index, top_hashtags.values, color='skyblue')

# Step 9: Add labels and title to the chart
# Label the x-axis as 'Hashtag', the y-axis as 'Amount', and add a title to the plot.
plt.xlabel('Hashtag')
plt.ylabel('Amount')
plt.title('Top 10 Most Used Hashtags (First 500,000 rows)')

# Step 10: Adjust the x-axis labels to avoid overlapping
# Rotate the x-axis labels (hashtags) by 45 degrees to make them readable and align them to the right.
plt.xticks(rotation=45, ha='right')

# Step 11: Optimize layout to ensure everything fits well
# Adjust the layout to prevent the chart elements from being cut off or overlapping.
plt.tight_layout()

# Step 12: Display the plot
# Show the final bar chart.
plt.show()
