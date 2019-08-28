#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    recipe_length = len(recipe)
    results = []
    ingredients_length = len(ingredients)
    if recipe_length > ingredients_length:
        return 0
    else:
        for key in recipe:
            if key in ingredients:
                ingredient_value = ingredients.get(key)
                recipe_value = recipe.get(key)
                ingredient_times = ingredient_value//recipe_value
                results.append(ingredient_times)
    lowest = results[0]
    for i in range(1, len(results)):
        if results[i] == 0:
            return 0
        else:
            if results[i] < lowest:
                lowest = results[i]
    return lowest



if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
