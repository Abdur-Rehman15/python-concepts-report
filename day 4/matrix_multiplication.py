# ========= list vs numpy matrix multiplication ============
import time
import numpy as np

matrix1 = [[1, 2, 3], [3, 4, 3]]

matrix2 = [[2, 3], [4, 5], [7, 8]]


def measure_time(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print("Execution Time:", t2 - t1, "secs")
        return result

    return wrapper


@measure_time
def multiply_simple_matrices(mat1, mat2):
    res_matrix = []

    # 1d vectors both
    if not isinstance(mat1[0], list) and not isinstance(mat2[0], list):
        if len(mat1) != len(mat2):
            raise ValueError("different lengths")
        for i in range(len(mat1)):
            res_matrix.append(mat1[i] * mat2[i])

    # 2d vectors both
    elif isinstance(mat1[0], list) and isinstance(mat2[0], list):
        if len(mat1[0]) == len(mat2):
            for i in range(len(mat1)):
                temp = []
                for j in range(len(mat2[0])):
                    sum = 0
                    for k in range(len(mat2)):
                        sum += mat1[i][k] * mat2[k][j]
                    temp.append(sum)

                res_matrix.append(temp)

        else:
            raise ValueError("non compatible..multiplication not possible")

    else:
        raise ValueError("1d and 2d cant multiply with each other")

    return res_matrix


print("\n---without numpy---")
print(multiply_simple_matrices(matrix1, matrix2))

arr1 = np.array(matrix1)
arr2 = np.array(matrix2)


@measure_time
def multiply_numpy_matrices(mat1, mat2):
    return mat1 @ mat2


print("\n---with numpy---")
print(multiply_numpy_matrices(arr1, arr2))