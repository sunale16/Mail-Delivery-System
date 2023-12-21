row_limit = count(array)
if row_limit > 0:
    column_limit = count(array[0])
    for x in range(max(0, i-1), min(i+1, row_limit)):
        for y in range(max(0, j-1), min(j+1, column_limit)):
            if x != i or y != j:
                print(array[x][y])
