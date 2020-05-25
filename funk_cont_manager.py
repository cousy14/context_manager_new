from cont_manager import time_pro

def dict_preparation(book_name, log_name):
  with time_pro(log_name):
    with open(book_name, encoding='UTF-8') as file:
      cook_of_dishes = {}
      for line in file:
        dish_name = line[:-1]
        counter = file.readline().strip()
        dishes = []
        for value in range(int(counter)):
          structure_of_dishes = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
          ingridients = file.readline().strip().split('|')
          for structure in ingridients:
            structure_of_dishes['ingredient_name'] = ingridients[0]
            structure_of_dishes['quantity'] = ingridients[1]
            structure_of_dishes['measure'] = ingridients[2]
          dishes.append(structure_of_dishes)
          cook_book = {dish_name: dishes}
          cook_of_dishes.update(cook_book)
        file.readline()

    return (cook_of_dishes)

print(dict_preparation('cook_book.txt', 'test_name_1_context.txt'))