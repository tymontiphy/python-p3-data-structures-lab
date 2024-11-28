spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return a list of names of strings with the names of each spicy food."""
    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    """Return a list of dictionaries with spicy foods with a heat_level over 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    """Print the names of each spicy food."""
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method"""
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)
    pass

def print_spiciest_foods(spicy_foods):
    """ONLY the spicy foods that have a heat level over 5 will be printed"""
    for food in get_spiciest_foods(spicy_foods):
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    pass

def get_average_heat_level(spicy_foods):
    """Return the average heat level of all spicy foods."""
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level / len(spicy_foods) if spicy_foods else 0.0
    pass

def create_spicy_food(spicy_foods, spicy_food):
    """Add a new spicy food to the list of spicy foods."""
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
