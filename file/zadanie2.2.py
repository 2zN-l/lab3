def calc(u, v, k):
    a, b = u, v
    for _ in range(2, k + 1):
        a_k = 2 * b + a
        b_k = 2 * b ** 2 + b
        a, b = a_k, b_k
    return a, b