# TODO Напишите функцию для поиска индекса товара
def search_index(product_list, product):
    if product in product_list:
        index_product = product_list.index(product)
    else:
        index_product = None
    return index_product


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_index(items_list, find_item)
    print(index_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
