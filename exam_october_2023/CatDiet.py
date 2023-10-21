percentage_fat = int(input())
percentage_proteins = int(input())
percentage_carbohydrates = int(input())
number_of_calories = int(input())
percentage_water = int(input())

total_fat_grams = ((percentage_fat / 100) * number_of_calories) / 9
total_proteins_grams = ((percentage_proteins / 100) * number_of_calories) / 4
total_carbohydrates_grams = ((percentage_carbohydrates / 100) * number_of_calories) / 4

total_food_grams = total_proteins_grams + total_carbohydrates_grams + total_fat_grams
total_calories_per_garms = number_of_calories / total_food_grams

percentage_food_no_water = 100 - percentage_water

result = total_calories_per_garms * (percentage_food_no_water / 100)

print(f'{result:.4f}')