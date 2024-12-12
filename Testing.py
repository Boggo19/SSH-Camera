from QueryFunction import connect_to_db, get_top_recipes

# Test connect_to_db function
def test_connect_to_db():
    print("Testing connect_to_db...")
    try:
        connect_to_db()
        print("Output: Connection successful")
    except Exception as e:
        print(f"Output: {e}")
    print()

# Test get_top_recipes function with mock data
def test_get_top_recipes():
    print("Testing get_top_recipes...")
    
    conn, cursor = connect_to_db()
    
    # Test 1
    ingredients = ["tomato", "cheese", "basil"]
    expected = [('Margherita Pizza', 1), ('Eggplant Parmesan', 1), ('Quinoa Salad', 1), ('Minestrone Soup', 1), ('Meatballs', 1)]
    actual = [recipe for recipe in get_top_recipes(cursor, ingredients)]
    print(f"Test Case 1")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print(f"Pass: {expected == actual}")
    print()
    
    
    
    # Test 2
    
    expected = []
    ingredients = ["cheese","curry sauce"]
    actual = get_top_recipes(cursor, ingredients)
    print(f"Test Case 2: No results")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print(f"Pass: {expected == actual}")
    print()

# Run the tests
test_connect_to_db()
test_get_top_recipes()
