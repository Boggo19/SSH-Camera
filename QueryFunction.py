import psycopg2


def connect_to_db():
    # Database configuration details
    DATABASE_CONGFIG = {
        'dbname' : 'SSHiverMeTimbers',
        'user' : 'postgres',
        'password' : 'Aun28012005',
        'host' : 'localhost',
        'port' : '5432',
    }

    try: 
        #connection to the database
        connection = psycopg2.connect(**DATABASE_CONGFIG)
        cursor = connection.cursor()
        print("Database connection successful")
        selectQuery = """
        SELECT recipe_id, ingredient_id
        FROM "SSH2".linking
        WHERE recipe_id = %s
        """
        cursor.execute(selectQuery, (4,))
        rows = cursor.fetchall()
        for row in rows:
            print(f"Recipe ID: {row[0]}, Ingredient ID: {row[1]}")

        # cursor.execute("SELECT version();")
        # version = cursor.fetchone()
        # print("PostgreSQL Version:",version)
    
    except Exception as e:
        print("Error connecting to database:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Database connection closed")



def get_ingredients(cursor):
    data = [
        ('Red Pepper', 2),
        ('Chicken', 1),
        ('Green Pepper', 3),
        ('Onion', 2),
        ('Bacon', 6),
        ('Red Pepper', 2),
        ('Chicken', 1),
        ('Green Pepper', 3),
        ('Onion', 2),
        ('Bacon', 6)
    ]
    return data   
    

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
    # conn, cursor = connect_to_db()
    # print("Connected to the database successfully.")
        
    # Fetch ingredients from camera
    ingredients = []
        
    # Fetch recipes
    # recipes = get_recipes(cursor, ingredients)
        
    # pass recipes to front end
    connect_to_db()
except Exception as e:
    print("An error occurred:", e)
