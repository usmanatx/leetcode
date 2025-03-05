def second_minimum(arr):
    second = arr[1]
    first = arr[0]
    for n in arr:
        if n < first:
            first = n
        if n < second and n > first:
            second = n
    return second
  
second_minimum([-2, 4, 5, -1, 2, 3, 0, -4, 1, 99, -6, -5, -19])
