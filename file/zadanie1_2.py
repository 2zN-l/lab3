
import time

start1 = time.perf_counter() 


def find3(obj, target):
    stack = [(obj, 0)]
    while stack:
        current_list, base_index = stack.pop()
        for i, item in enumerate(current_list):
            if item == target:
                return base_index + i
            if isinstance(item, list):
                stack.append((item, base_index + i))
    
    return None

print(find3([1, 2, [3, 4, [5, [6, []]]]], 4)) 
print(find3([1, 2, [3, 4, [5, [6, []]]]], 'spam')) 



end1 = time.perf_counter()
print(f"Время: {end1 - start1:.6f} сек")

#==========================================
start2 = time.perf_counter() 



def find4(obj, target):
    stack = [(obj, 0)]
    while stack:
        current, base = stack.pop()
        for i, item in enumerate(current):
            if item == target:
                return base + i
            if isinstance(item, list):
                stack.append((item, base + i))
    return None

print(find4([1, 2, [3, 4, [5, [6, []]]]], 4))
print(find4([1, 2, [3, 4, [5, [6, []]]]], 'spam'))


end2 = time.perf_counter()
print(f"Время: {end2 - start2:.6f} сек")
print(f'Время выполнения улучшена в:{round((end1 - start1)/(end2 - start2), 2)}')