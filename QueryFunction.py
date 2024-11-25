def connect_to_db():
    pass

def get_recipes(cursor, ingredients):
    ingredient_count = len(ingredients)
    query = """
        SELECT r.RecipeName
        FROM Recipes r
        JOIN RecipeIngredients ri ON r.RecipeID = ri.RecipeID
        JOIN Ingredients i ON ri.IngredientID = i.IngredientID
        WHERE i.IngredientName = ANY(%s)
        GROUP BY r.RecipeID, r.RecipeName
        HAVING COUNT(DISTINCT i.IngredientID) = %s;
    """
    try:
        cursor.execute(query, (ingredients, ingredient_count))
        return [row[0] for row in cursor.fetchall()]
    except:
        print("Error executing query:")
        raise


try:
    # Connect to database
    conn, cursor = connect_to_db()
    print("Connected to the database successfully.")
        
    # Fetch ingredients from camera
    ingredients = []
        
    # Fetch recipes
    recipes = get_recipes(cursor, ingredients)
        
    # pass recipes to front end
except Exception as e:
    print("An error occurred:", e)
