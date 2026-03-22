import time

start1 = time.perf_counter() 


def calc3(u, v, k):
    a, b = u, v
    for i in range(2, k + 1):
        a_k = 2 * b + a
        b_k = 2 * b ** 2 + b
        a, b = a_k, b_k
    return a, b

print(calc3 (3, 2, 4))

end1 = time.perf_counter()
print(f"Время: {end1 - start1:.6f} сек")

#==========================================
start2 = time.perf_counter() 



def calc4(u, v, k):
    a, b = u, v
    for i in range(2, k + 1):
        a, b = 2 * b + a, 2 * b * b + b
    return a, b

print(calc4(3, 2, 4))

end2 = time.perf_counter()
print(f"Время: {end2 - start2:.6f} сек")
print(f'Время выполнения улучшена в:{round((end1 - start1)/(end2 - start2), 2)}')