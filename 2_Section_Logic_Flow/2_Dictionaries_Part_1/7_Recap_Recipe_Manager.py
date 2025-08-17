"""
You are managing a digital recipe book where each recipe is stored as a dictionary.
Each dictionary contains the name of the recipe as the key and a list of ingredients as the value.
Your task is to perform several operations to update and manage the recipe book.

Create the Recipe Book:
Create a dictionary named recipe_book with the following recipes:
"Pancakes": ["flour", "milk", "eggs", "sugar"]
"Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
Access Ingredients:
Print the list of ingredients for "Pancakes".
Add a New Recipe:
Add a new recipe "Smoothie" with the ingredients ["banana", "milk", "honey"] to the dictionary.
Modify a Recipe:
Add "blueberries" to the "Smoothie" recipe.
Print All Recipes:
Print the entire recipe_book dictionary to verify the updates.
"""

recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}

print(recipe_book["Pancakes"])

recipe_book["Smoothie"] = ["banana", "milk", "honey"]
recipe_book["Smoothie"].append("blueberries")

print(recipe_book)

"""
To add an item to an existing list without replacing the entire list, you should use a list method specifically designed for this purpose.
The append() method is commonly used to add a single item to the end of a list.

Consider how you would use append() on the list that is the value associated with the "Smoothie" key in your recipe_book dictionary.

For example, if you had a list my_list = [1, 2], and you wanted to add 3 to it, you would use my_list.append(3), which would result in my_list becoming [1, 2, 3].
"""