def calc(u, v, k):
    if k == 1:
        return u, v
    else:
        a_k_1, b_k_1 = calc(u, v, k - 1)
        a_k = 2 * b_k_1 + a_k_1
        b_k = 2 * b_k_1 ** 2 + b_k_1
        return a_k, b_k
