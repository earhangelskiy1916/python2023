def print_operation_table(operation, num_rows=int(input("введите кол-во строк ")), num_columns=int(input("введите кол-во столбцов "))):
    op = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in op:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)