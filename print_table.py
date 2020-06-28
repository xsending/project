tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table_data):
    count = len(table_data[0])
    column_width = [0] * len(table_data)

    for i in range(len(table_data)):
        for n in range(count):
            for word in table_data[i]:
                maximum = len(table_data[i][n])
                if len(word) > maximum:
                    maximum = len(word)
                    column_width[i] = maximum

    for y in range(count):
        for x in range(len(table_data)):
            print(f"{table_data[x][y]}".rjust(column_width[x]), end=' ')
            if x == 2:
                print()


print_table(tableData)
