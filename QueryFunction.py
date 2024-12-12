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
            port="5432"              # Replace with your port, if different
        )
        return conn, conn.cursor()
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        raise

def getIngredients():
    conn, cursor = connect_to_db()
    ingredients = get_ingredients(cursor)
    cursor.close()
    conn.close()
    return ingredients

def get_ingredients(cursor):
    query = """
    SELECT i.ingredient_name
    FROM "SSH".ingredients i
    ORDER BY RANDOM()
    LIMIT 30
    """

    try:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]
    except psycopg2.Error as e:
        print("Error executing query:", e)
        raise

def getRecipeInfo(recipeName):
    conn, cursor = connect_to_db()
    recipeInfo = get_recipe_info(cursor, recipeName)
    cursor.close()
    conn.close()
    return recipeInfo

def get_recipe_info(cursor, recipeName):
    query = """
            SELECT r.recipe_name, r.image_data, r.description, r.kcal, r.protein, r."carbs(sugar)", r."fat(saturates)", r.fibre, r.salt, r.prep_time, r.cook_time, r.instructions
            FROM "SSH".recipes r
            WHERE r.recipe_name = (%s)
            """

    try:
        cursor.execute(query, (recipeName,))
        return cursor.fetchall()
    except psycopg2.Error as e:
        print("Error executing query:", e)
        raise

def getRecipeIngredients(recipeName):
    conn, cursor = connect_to_db()
    ingredients = get_recipe_ingredients(cursor, recipeName)
    cursor.close()
    conn.close()
    return ingredients

def get_recipe_ingredients(cursor, recipeName):
    query = """
            SELECT i.ingredient_name
            FROM "SSH".ingredients i
            INNER JOIN "SSH".linking l ON i.ingredient_id = l.ingredient_id
            INNER JOIN "SSH".recipes r ON l.recipe_id = r.recipe_id
            WHERE r.recipe_name = (%s)"""
    
    try:
        cursor.execute(query, (recipeName,))
        return cursor.fetchall()
    except psycopg2.Error as e:
        print("Error executing query:", e)
        raise

def getRecipes(ingredients):
    conn, cursor = connect_to_db()
    recipes = get_top_recipes(cursor, ingredients)
    cursor.close()
    conn.close()
    return recipes

def get_top_recipes(cursor, ingredients):
    """
    Queries the database for the top 5 most suitable recipes based on the user's fridge ingredients.
    :param cursor: The database cursor
    :param ingredients: List of ingredient names (e.g., ["Tomato", "Cheese", "Basil"])
    :return: List of the top 5 recipe names with relevance scores
    """
    # Query to find exact matches
    exact_match_query = """
        SELECT r.recipe_name
        FROM "SSH".recipes r
        JOIN "SSH".linking l ON r.recipe_id = l.recipe_id
        JOIN "SSH".ingredients i ON l.ingredient_id = i.ingredient_id
        WHERE i.ingredient_name = ANY(%s) AND i.fridge_item = TRUE
        GROUP BY r.recipe_id, r.recipe_name
        HAVING COUNT(DISTINCT i.ingredient_id) = (
            SELECT COUNT(DISTINCT l2.ingredient_id)
            FROM "SSH".linking l2
            JOIN "SSH".ingredients i2 ON l2.ingredient_id = i2.ingredient_id
            WHERE l2.recipe_id = r.recipe_id AND i2.fridge_item = TRUE
        )
        LIMIT 5;
    """

    # Query to find partial matches if no exact matches are found
    partial_match_query = """
        SELECT r.recipe_name, COUNT(DISTINCT i.ingredient_id) AS match_count
        FROM "SSH".recipes r
        JOIN "SSH".linking l ON r.recipe_id = l.recipe_id
        JOIN "SSH".ingredients i ON l.ingredient_id = i.ingredient_id
        WHERE i.ingredient_name = ANY(%s) AND i.fridge_item = TRUE
        GROUP BY r.recipe_id, r.recipe_name
        ORDER BY match_count DESC
        LIMIT 5;
    """

    try:
        # Execute the exact match query
        cursor.execute(exact_match_query, (ingredients,))
        results = cursor.fetchall()
        
        
        # Otherwise, execute the partial match query
        cursor.execute(partial_match_query, (ingredients,))
        partial_results = cursor.fetchall()

        recipes = results + partial_results
        return recipes[:5]

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
        
        # Fetch top recipes
        recipes = get_top_recipes(cursor, ingredients)
        
        # Display results
        if recipes:
            print("\nTop Recipes:")
            for recipe, description in recipes:
                print(f"- {recipe} ({description})")
        else:
            print("\nNo recipes found.")
    
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
