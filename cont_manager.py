import datetime


class time_pro():

    def __init__(self, log_path):
        self.log_path = log_path

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        self.log = open(self.log_path, 'a', encoding='utf-8')
        self.log.write(f'Время запуска кода: {datetime.datetime.now()}\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.write(f'Время окончания работы кода: {datetime.datetime.now()}\n')
        self.log.write(f'Время работы кода: {datetime.datetime.now() - self.start_time}\n')
        self.log.close()
