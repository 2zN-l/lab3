import time

start1 = time.perf_counter() 


def find(obj, target, current_index=0):
    for i, item in enumerate(obj):
        if item == target:
            return current_index + i
        if isinstance(item, list):
            result = find(item, target, current_index + i)
            if result is not None:
                return result
    return None


print(find([1, 2, [3, 4, [5, [6, []]]]], 4)) 
print(find([1, 2, [3, 4, [5, [6, []]]]], 'spam')) 



end1 = time.perf_counter()
print(f"Время: {end1 - start1:.6f} сек")

#==========================================
start2 = time.perf_counter() 



def find(obj, target, idx=0):
    for i, x in enumerate(obj):
        if x == target:
            return idx + i
        if isinstance(x, list):
            res = find(x, target, idx + i)
            if res is not None:
                return res
    return None

print(find([1, 2, [3, 4, [5, [6, []]]]], 4))
print(find([1, 2, [3, 4, [5, [6, []]]]], 'spam'))


end2 = time.perf_counter()
print(f"Время: {end2 - start2:.6f} сек")
print(f'Время выполнения улучшена в:{round((end1 - start1)/(end2 - start2), 2)}')