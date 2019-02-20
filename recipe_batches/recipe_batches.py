#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
		maxSingleServings = None
		for ingredient, quantity in recipe.items():
				print(f"{ingredient}-{quantity}")
				for availableIngredient, availableQuantity in ingredients.items():
						if ingredient == availableIngredient:
								print(f"{ingredient}")
								if quantity > availableQuantity:
									print(f"{ingredient} is about to return 0")
									return 0
								maxSingle = availableQuantity // quantity
								print(f"{maxSingle}")
								if maxSingleServings == None:
									temp = maxSingle
									maxSingleServings = temp
									print(f"hello i'm maxSingle: {maxSingleServings}")
								elif maxSingle > maxSingleServings:
									pass
						else:
								temp = 0
								maxSingle = temp
								pass
		print(f"hello!!!!!! i'm maxSingle: {maxSingleServings}")
		return maxSingleServings


if __name__ == '__main__':
				# Change the entries of these dictionaries to test
				# your implementation with different inputs
		recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
		ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
		print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
				batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# self.assertEqual(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }), 0)
# self.assertEqual(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }), 1)
# self.assertEqual(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }), 2)
# self.assertEqual(recipe_batches({ 'milk': 2 }, { 'milk': 200}), 100)


