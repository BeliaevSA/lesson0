import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline():
            line = file.readline()
            print(line)
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# time_start = time.time()
# print('старт')
# for filename in filenames:
#     read_info(filename)
# time_finish = time.time()
# print('Время линейного выполнения', time_finish - time_start)

if __name__ == '__main__':
    time_start = time.time()
    with Pool(4) as pool:
        results = pool.map(read_info, filenames)
    time_finish = time.time()
    print('Время многопроцессного выполнения', time_finish - time_start)