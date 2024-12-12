import psycopg2

# Connect to the database
conn = psycopg2.connect(dbname="SSHiverMeTimbers", user="postgres", password="password", host="localhost", port="5432")
cur = conn.cursor()

# Fetch the binary data
cur.execute('SELECT image_data FROM "SSH".recipes WHERE recipe_id = %s', (33,))
binary_data = cur.fetchone()[0]

# Save the binary data as an image file
with open("output_image.png", "wb") as file:
    file.write(binary_data)

cur.close()
conn.close()
