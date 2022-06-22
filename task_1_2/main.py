import os
import pprint

FILE_NAME = "recipes.txt"
BASE_PATH = os.getcwd()
full_path = os.path.join(BASE_PATH, FILE_NAME)

def recipes_reader(file):
    try:
        with open(file, 'r', encoding='utf-8') as file_obj:
            cook_book = {}
            for line in file_obj:
                if line.isspace():
                    continue
                elif len(line.strip()) > 0:
                    recipes = line.strip()
                    cook_book[recipes] = []
                    quantity_ingredients = file_obj.readline()
                    for item in range(int(quantity_ingredients)):
                        ingredient_list = file_obj.readline().strip().split('|')
                        ingredient_name = ingredient_list[0].strip()
                        quantity = int(ingredient_list[1].strip().strip())
                        measure = ingredient_list[-1].strip()
                        dict_name = {'ingredient_name': ingredient_name,
                                     'quantity': quantity,
                                     'measure': measure}
                        cook_book[recipes].append(dict_name)
                    file_obj.readline()
            return cook_book
    except FileNotFoundError:
        content = 'Файл не найден'
        return content

def get_shop_list_by_dishes(dishes, person_count):
    dict_by_dishes = {}
    for dishe in dishes:
        for key, value_list_Ingredients in recipes_reader(full_path).items():
            if dishe.lower() == key.lower():
                for value_dict_ingredients in value_list_Ingredients:
                    ingredient = value_dict_ingredients['ingredient_name']
                    if ingredient in dict_by_dishes.keys():
                        dict_by_dishes[ingredient]['quantity'] += (value_dict_ingredients['quantity'] * person_count)
                    else:
                        dict_by_dishes.setdefault(value_dict_ingredients['ingredient_name'], {})
                        new_value_dict_ingredients = {'measure': value_dict_ingredients['measure'],
                                                      'quantity': value_dict_ingredients['quantity'] * person_count}
                        dict_by_dishes[ingredient] = new_value_dict_ingredients
    return dict_by_dishes


pprint.pprint(recipes_reader(full_path), width=200)
print('=' * 100)
pprint.pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))