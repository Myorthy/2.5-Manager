#Задача из темы 2.4(Работа с файловой системой)
import time

class TimeOpen:

    def __init__(self, file_path):

        self.file_path = file_path

    def __enter__(self):
        self.start_time = time.time()
        self.time_1 = time.strftime("%d.%b %H:%M:%S")

        self.file = open(self.file_path, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.time_2 = time.strftime("%d.%b %H:%M:%S")
        print(f'Время начало выполнения программы: {self.time_1}')
        print(f'Время окончания выполнения программы: {self.time_2}')
        print(f'На выполнение программы потрачено {round(self.end_time - self.start_time, 5)} сек')
        self.file.close()

if __name__ == '__main__':
    with TimeOpen('dishes.txt') as list_dishes:
        cook_book = {}
        for dish in list_dishes:
            key = dish.strip()
            count = int(list_dishes.readline())
            values = list()
            for i in range(count):
                value = list_dishes.readline().strip()
                value = value.split(' | ')
                value_dict = {'ingridient_name': value[0], 'quantity': int(value[1]), 'measure': value[2]}
                values.append(value_dict)
            list_dishes.readline()
            cook_book.update({key : values})
        print(cook_book)
