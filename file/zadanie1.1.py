def find(obj, target, current_index=0):
    for i, item in enumerate(obj):
        if item == target:
            return current_index + i
        if isinstance(item, list):
            result = find(item, target, current_index + i)
            if result is not None:
                return result
    return None