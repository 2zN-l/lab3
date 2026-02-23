def find(obj, target):
    stack = [(obj, 0)]
    while stack:
        current_list, base_index = stack.pop()
        for i, item in enumerate(current_list):
            if item == target:
                return base_index + i
            if isinstance(item, list):
                stack.append((item, base_index + i))
    
    return None