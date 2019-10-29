def to_bin(x):
    output = bin(x)[2:]
    return output[::-1]


def to_dec(x):
    return int(x, 2)


def des(x, s_box):
    row = to_dec(x[0] + x[-1])
    column = to_dec(x[1:5])
    output = s_box[row][column]
    print("row is ", row)
    print("colum is", column)
    print("output is", output)


x = '110111'
s_box = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1,3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
des(x, s_box)