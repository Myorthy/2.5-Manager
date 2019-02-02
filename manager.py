import time

class TimeOpen:

    def __init__(self, file_path):

        self.file_path = file_path

    def __enter__(self):
        self.start_time = time.time()
        self.time_1 = time.strftime("%d.%b %H:%M:%S")

        self.file = open(self.file_path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.time_2 = time.strftime("%d.%b %H:%M:%S")
        print(f'Время начало выполнения программы: {self.time_1}')
        print(f'Время окончания выполнения программы: {self.time_2}')
        print(f'На выполнение программы потрачено {round(self.end_time - self.start_time, 5)} сек')
        self.file.close()

if __name__ == '__main__':
    with TimeOpen('class.py') as file:
        f = file.read()
