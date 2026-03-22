import time

start1 = time.perf_counter() 


def calc1(u, v, k):
    if k == 1:
        return u, v
    else:
        a_k_1, b_k_1 = calc1(u, v, k - 1)
        a_k = 2 * b_k_1 + a_k_1
        b_k = 2 * b_k_1 ** 2 + b_k_1
        return a_k, b_k
    

print(calc1 (3, 2, 4))


end1 = time.perf_counter()
print(f"Время: {end1 - start1:.6f} сек")

#==========================================
start2 = time.perf_counter() 



def calc2(u, v, k):
    if k == 1:
        return u, v
    a, b = calc2(u, v, k - 1)
    return 2 * b + a, 2 * b * b + b


print(calc2 (3, 2, 4))


end2 = time.perf_counter()
print(f"Время: {end2 - start2:.6f} сек")
print(f'Время выполнения улучшена в:{round((end1 - start1)/(end2 - start2), 2)}')