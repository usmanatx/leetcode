def find_first_non_repeating(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    
    for x in arr:
        if counts[x] == 1:
            return x
    return None
