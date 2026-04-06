


# Исходная функция (для сравнения)
def calc1(u, v, k):
    def a(k):
        if k == 1:
            return u
        return 2 * b(k - 1) + a(k - 1)
    
    def b(k):
        if k == 1:
            return v
        return 2 * (b(k - 1) ** 2) + b(k - 1)
    
    return a(k), b(k)

# Оптимизированная функция


def calc1_optimized(u, v, k):
    def recurse(n):
        if n == 1:
            return (u, v)
        a_prev, b_prev = recurse(n - 1)
        a_cur = 2 * b_prev + a_prev
        b_cur = 2 * (b_prev ** 2) + b_prev
        return (a_cur, b_cur)
    
    return recurse(k)





import time

k = 20 
u = 1
v = 1
start_time_1 = time.time()
calc1(u, v, k)
end_time_1 = time.time()
print(f"Время выполнения исходной функции для k={k}: {end_time_1 - start_time_1:.6f} секунд")

start_time_2 = time.time()
calc1_optimized(u, v, k)
end_time_2 = time.time()
print(f"Время выполнения оптимизированной функции для k={k}: {end_time_2 - start_time_2:.6f} секунд")

t= (end_time_1 - start_time_1)/(end_time_2 - start_time_2)
print(f"Ускорено: {t}")