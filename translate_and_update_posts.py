from transformers import MarianMTModel, MarianTokenizer
import mysql.connector

# Step 1: Initialize MarianMT model and tokenizer
# The MarianMT model and tokenizer are loaded from the Hugging Face model repository ("Helsinki-NLP/opus-mt-tc-big-he-en").
# This specific model translates text from Hebrew to English.
model_name = "Helsinki-NLP/opus-mt-tc-big-he-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Step 2: Define a function to translate text using the MarianMT model
# The function takes text input, tokenizes it, generates the translation, and decodes the result into a readable string.
def translate_text(text):
    # Tokenize the input text and feed it to the translation model.
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    # Decode the translated text and return it.
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translated_text

# Step 3: Connect to MySQL database
# Establish a connection to a MySQL database using the provided credentials.
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'fp_db'  # The database where the posts are stored
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Step 4: Fetch text data from MySQL database where 'translated' column is null
# Retrieve rows from the 'posts_new' table where the 'translated' column is currently NULL (meaning the text hasn't been translated yet).
query = "SELECT id, img_description FROM posts_new WHERE translated IS NULL"
cursor.execute(query)
rows = cursor.fetchall()

# Step 5: Translate and update the text data in the database
# Iterate over each row, translating the text and updating the corresponding record in the database with the translated text.
for row in rows:
    id, text = row
    # Translate the text from Hebrew to English using the 'translate_text' function.
    translated_text = translate_text([text])[0]  # Translate the single text input
    # Prepare the SQL query to update the 'translated' column with the translated text.
    update_query = "UPDATE posts_new SET translated = %s WHERE id = %s"
    # Execute the query to update the translated text in the database.
    cursor.execute(update_query, (translated_text, id))
    # Commit the changes to the database to ensure they are saved.
    conn.commit()

# Step 6: Close cursor and database connection
# Close the cursor and database connection to free up resources after the process is complete.
cursor.close()
conn.close()
