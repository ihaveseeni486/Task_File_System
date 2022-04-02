def fill_cook_book(cook_book):
    with open("files/recipes.txt", encoding='utf-8') as file:
        int_count_rows_recipy = 0
        current_recipy_name = ""
        for line in file:
            str_got = line.strip()
            if str_got == "":
                continue
            try:
                str_got = int(str_got)
            except:
                exc = "Не получилось преобразовать строку"
            if isinstance(str_got, int):
                # строка с количеством ингридиентов
                int_count_rows_recipy = str_got
            elif isinstance(str_got, str) and int_count_rows_recipy == 0:
                # название рецепта
                current_recipy_name = str_got
                cook_book[str_got] = []
            else:
                # ингр кол-во мера
                ingr_name = str_got.split('|')[0].strip()
                ingr_count = int(str_got.split('|')[1].strip())
                ingr_mera = str_got.split('|')[2].strip()
                ingrid_dict = {}
                ingrid_dict['ingredient_name'] = ingr_name
                ingrid_dict['quantity'] = ingr_count
                ingrid_dict['measure'] = ingr_mera
                cook_book[current_recipy_name].append(ingrid_dict)
                int_count_rows_recipy -= 1
    return cook_book


def get_shop_list_by_dishes(recipies, count):
    cook_book = {}
    cook_book = fill_cook_book(cook_book)
    need_to_buy = {}
    for recipy in recipies:
        spec = cook_book.get(recipy, 0)
        if spec == 0:
            print(f"Рецепт {recipy} не записан в книге рецептов")
        else:
            for ingr in spec:
                if ingr['ingredient_name'] in need_to_buy.keys():
                    a = ingr.value()
                    a['quantity'] = int(a['quantity']) + int(ingr['quantity']) * count
                else:
                    minidict = {}
                    minidict['measure'] = ingr['measure']
                    minidict['quantity'] = int(ingr['quantity']) * count
                    need_to_buy[ingr['ingredient_name']] = minidict
    return need_to_buy


if __name__ == '__main__':
    recipies_needed = ['Запеченный картофель', 'Омлет']
    count = 2
    ntb = get_shop_list_by_dishes(recipies_needed, count)
    for key, value in ntb.items():
        print(f"{key}: {value}")
