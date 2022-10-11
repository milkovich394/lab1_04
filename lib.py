def matrixsozd():
    matrix = list()
    n = int(input('Введите кол-во входных списков '))
    while n > 0:
        matrix.append(input('Введите элементы списка через пробел.\n').split(' '))
        n -=1
    return matrix

def povtorenia():
    matrix = matrixsozd()
    i = 0
    index = 0
    min = len(matrix)
    for spisok in matrix:
        if len(spisok) > min:
            min = len(spisok)
            index = i
        i += 1
    povtor = list()
    run = True
    j = 0
    i = 0
    while run:
        try:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] in matrix[i+1]:
                        if matrix[i] in povtor:
                            None
                        else:
                            povtor.append(matrix[i][j])
        except IndexError:
            run = False
    if len(povtor) > 0:
        print('Повторяюшееся символы ',povtor)
    else:
        print('Повторений нет!')