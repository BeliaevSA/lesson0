from threading import Thread
import time

def write_words(word_count, file_name):
  for i in range(1, word_count+1):
    with open(file_name, 'a', encoding='utf-8') as file:
      file.write(f'Какое-то слово №{i}\n')
    time.sleep(0.1)
  print(f'Завершилась запись в файл {file_name}')

start_time_work_func = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time_work_func = time.time()
print(f'Работа функций: {round(finish_time_work_func - start_time_work_func, 1)}сек')

thread_write_words_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_write_words_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_write_words_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_write_words_4 = Thread(target=write_words, args=(100, 'example8.txt'))

start_time_work_thread = time.time()
thread_write_words_1.start()
thread_write_words_1.join()
thread_write_words_2.start()
thread_write_words_2.join()
thread_write_words_3.start()
thread_write_words_3.join()
thread_write_words_4.start()
thread_write_words_4.join()
finish_time_work_thread = time.time()

print(f'Работа потоков: {round(finish_time_work_thread - start_time_work_thread, 1)}')
