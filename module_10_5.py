# Многопроцессное программирование
import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() == "":
                pass
            else:
                string_f = file.readline()
                all_data.append(string_f)


# start = datetime.datetime.now()
# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# read_info(filenames[0])
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])
# end = datetime.datetime.now()
# print(end - start) # 0:00:03.019014

if __name__ == '__main__':
    start1 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        pool.map(read_info, filenames)
    end1 = datetime.datetime.now()
    print(end1 - start1) # 0:00:01.291023