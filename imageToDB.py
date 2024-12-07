import os
import psycopg2

# Database connection parameters
conn = psycopg2.connect(
    dbname="SSHiverMeTimbers", 
    user="postgres", 
    password="password", 
    host="localhost", 
    port="5432"
)
cur = conn.cursor()

# Directory containing recipe images
image_directory = r"C:\Users\ahshe\SSH-Camera-1\recipe_images"

# Loop through all files in the image directory
for file_name in os.listdir(image_directory):
    # Extract the recipe name from the file (remove file extension)
    recipe_name = os.path.splitext(file_name)[0]

    # Build the full file path
    file_path = os.path.join(image_directory, file_name)

    # Read the binary data from the image file
    with open(file_path, "rb") as file:
        binary_data = file.read()

    try:
        # Update the recipe with the matching recipe_name
        cur.execute(
            'UPDATE "SSH".recipes SET image_data = %s WHERE LOWER(recipe_name) = LOWER(%s);',
            (binary_data, recipe_name)
        )
        print(f"Updated {recipe_name} with its corresponding image.")
    except Exception as e:
        print(f"Error updating {recipe_name}: {e}")

# Commit all changes and close the connection
conn.commit()
cur.close()
conn.close()

print("All images have been inserted successfully.")
