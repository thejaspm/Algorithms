def max_sum_sqr_sub_matrix(m, n, arr):
    t = [[0] * (n + 1) for i in range(0, m + 1)]
    g_max = 0

    def getmin(i, j):
        return min(t[i][j], t[i + 1][j], t[i][j + 1])

    for i in range(0, m):
        for j in range(0, n):
            if arr[i][j] == 0:
                t[i + 1][j + 1] = 0
            else:
                t[i + 1][j + 1] = getmin(i, j) + 1
                if g_max < t[i + 1][j + 1]:
                    g_max = t[i + 1][j + 1]
    print(g_max)


def largestMatrix(arr):
    m, n = len(arr), len(arr[0])

    # to optimize space, we just need to  know the previous rows max sqr matrix locations
    # we toogle two rows with i%2 and access the previous one by (i-1)%2
    t = [[0 for j in range(n)] for i in range(2)]

    g_max = 0
    # first row is special case , put it as is
    for j in range(0, n):
        if arr[0][j] == 1:
            t[0][j] = 1
            g_max = max(g_max, 1)

    for i in range(1, m):
        # first column of each row is special case , put as is
        if arr[i][0] == 1:
            t[i % 2][0] = 1
            g_max = max(g_max, 1)
        else:
            t[i % 2][0] = 0

        for j in range(1, n):
            if arr[i][j] == 0:
                t[i % 2][j] = 0
            else:
                # calculate min of past 3 neighbours and add 1 
                t[i % 2][j] = min(t[i % 2][j - 1], t[(i - 1) % 2][j - 1], t[(i - 1) % 2][j]) + 1
                g_max = max(g_max, t[i % 2][j])
    print(g_max)


arr_1 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1],

]

max_sum_sqr_sub_matrix(3, 5, arr_1)

largestMatrix(arr_1)
