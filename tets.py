import threading
from queue import Queue
import multiprocessing

class FactorialThread(threading.Thread):
    def __init__(self, start, end, result_queue):
        threading.Thread.__init__(self)
        self.start = start
        self.end = end
        self.result_queue = result_queue

    def run(self):
        result = 1
        for i in range(self.start, self.end + 1):
            result *= i
        self.result_queue.put(result)

def parallel_factorial(n):
    # Разделим диапазон значений для каждого потока
    part = n // 3
    q = Queue()

    # Создаем три потока для вычисления факториала
    thread1 = FactorialThread(1, part, q)
    thread2 = FactorialThread(part + 1, 2 * part, q)
    thread3 = FactorialThread(2 * part + 1, n, q)

    # Запускаем все три потока
    thread1.start()
    thread2.start()
    thread3.start()

    # Дожидаемся завершения каждого потока
    thread1.join()
    thread2.join()
    thread3.join()

    # Извлекаем результаты из очереди
    result1 = q.get()
    result2 = q.get()
    result3 = q.get()

    # Закрываем очередь
    q.close()

    # Создаем три процесса для вычисления итогового результата
    process1 = multiprocessing.Process(target=mul, args=(result1, result2))
    process2 = multiprocessing.Process(target=mul, args=(result3, 1))
    process3 = multiprocessing.Process(target=mul, args=(process1, process2))

    # Запускаем процессы
    process1.start()
    process2.start()
    process3.start()

    # Дожидаемся завершения каждого процесса
    process1.join()
    process2.join()
    process3.join()

    # Возвращаем результат
    return process3.value

def mul(x, y):
    return x * y

# Запрос числа у пользователя
n = int(input("Введите число для вычисления факториала: "))

# Вызов функции для вычисления факториала
result = parallel_factorial(n)

# Вывод результата
print(f"{n}! = {result}")
