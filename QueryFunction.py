import psycopg2

def connect_to_db():
    """
    Establishes a connection to the PostgreSQL database and returns the connection and cursor.
    """
    try:
        conn = psycopg2.connect(
            dbname="SSHiverMeTimbers",  # Replace with your database name
            user="postgres",    # Replace with your database username
            password="changeme",  # Replace with your database password
            host="localhost",        # Replace with your host, if different
            port="5433"              # Replace with your port, if different
        )
        return conn, conn.cursor()
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        raise

def get_recipes(cursor, ingredients):
    """
    Queries the database for recipes that can be made with the given list of ingredients.
    :param cursor: The database cursor
    :param ingredients: List of ingredient names (e.g., ["Tomato", "Cheese", "Basil"])
    :return: List of recipe names that match the criteria
    """
    query = """
        SELECT r.recipe_name
        FROM "SSH2".recipes r
        JOIN "SSH2".linking l ON r.recipe_id = l.recipe_id
        JOIN "SSH2".ingredients i ON l.ingredient_id = i.ingredient_id
        WHERE i.ingredient_name = ANY(%s)
        GROUP BY r.recipe_id, r.recipe_name
        HAVING COUNT(DISTINCT i.ingredient_id) = (
            SELECT COUNT(DISTINCT l2.ingredient_id)
            FROM "SSH2".linking l2
            WHERE l2.recipe_id = r.recipe_id
        );
    """
    try:
        # Pass the list as a tuple by adding a comma after the list
        cursor.execute(query, (ingredients,))
        return [row[0] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        print("Error executing query:", e)
        raise

def main():
    """
    Main function to interact with the user and display recipes based on their available ingredients.
    """
    try:
        # Connect to the database
        conn, cursor = connect_to_db()
        print("Connected to the database successfully.")
        
        # Input ingredients from the user
        ingredients = input("Enter the ingredients you have, separated by commas: ").split(",")
        ingredients = [ingredient.strip() for ingredient in ingredients]  # Clean up whitespace
        
        # Fetch recipes
        recipes = get_recipes(cursor, ingredients)
        
        # Display results
        if recipes:
            print("\nRecipes you can make:")
            for recipe in recipes:
                print(f"- {recipe}")
        else:
            print("\nNo recipes found for the given ingredients.")
    
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Clean up database connection
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()
