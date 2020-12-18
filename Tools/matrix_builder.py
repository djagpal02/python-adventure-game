## This is not required or part of the game, it was simply used to generate large matrices to build the maps

def map_builder(x,y):
    """
    Matrix Generator
    ...

    Parameters 
    ----------
    :param x: number of columns
    :type x: int
    :param y: number of rows
    :type y: int

    Return
    ------
    :return matrix: large matrix containing tuples of required size
    :rtype matrix: list.list
    """
    matrix = []
    for i in range(y):
        list = []
        for j in range(x):
            list.append((10,"#####"))
        matrix.append(list)

    return matrix

# To print the matrices
a = map_builder(22,22)
for i in range(len(a)):
    print(a[i])
