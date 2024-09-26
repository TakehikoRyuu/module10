# Создание потоков

from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    word_count = int(word_count)
    with open(file_name, 'w+', encoding='utf-8') as file:
        for i in range(word_count):
            line = (f'Какое-то слово № {i+1}\n')
            file.write(line)
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start1 = datetime.now()
exa1 = write_words(10, 'example1.txt')
exa2 = write_words(30, 'example2.txt')
exa3 = write_words(200, 'example3.txt')
exa4 = write_words(100, 'example4.txt')
stop1 = datetime.now()
print(f'Работа потоков{stop1 - start1}')

start2 = datetime.now()
thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

stop2 = datetime.now()
print(f'Работа потоков {stop2 - start2}')