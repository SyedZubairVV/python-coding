def miniMaxSum(arr):
    arrsort = sorted(arr)
    min = 0
    max = 0
    for i in range(0, 4):
        min = min + arrsort[i]
    for i in range(1, 5):
        max = max + arrsort[i]
    print(min, max)
