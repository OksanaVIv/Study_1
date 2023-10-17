
size_mb = 1.44  # Объем дискеты

number_of_pages = 100
number_of_lines_per_pages = 50
number_of_symbols_per_lines = 25
memory_for_one_symbols = 4

symbols_per_book = number_of_symbols_per_lines * number_of_lines_per_pages * number_of_pages
memory_for_one_book = symbols_per_book * memory_for_one_symbols
size_bite = size_mb * 1024 * 1024
number_of_book = size_bite // memory_for_one_book

print("Количество книг, помещающихся на дискету:", int(number_of_book))
