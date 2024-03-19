list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(len(list_)):  # цикл работает на длину строки, т.е на количество элементов в списке
    cars_count += 10  # после каждой итерации цикла будет прибавлено 10 к переменной cars_count
    print(f'Я езжу на автомабиле марки: {list_[i]}')  # вывод строк, пока цикл не завершен
    print(cars_count)

