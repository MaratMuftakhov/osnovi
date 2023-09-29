# %% [markdown]
# <h1>Импорт библиотек

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# <h1>Задача 1. Дан набор из $p$ матриц размерностью $(n, n)$ и $p$ векторов размерностью $(n, 1)$, найти сумму произведений матриц на векторы. Написать тесты для кода

# %%
def sum_prod(X, V):
    if type(X) != np.ndarray or type(V) != np.ndarray:
        X = np.array(X)
        V = np.array(V)

    summa = sum(X.dot(i) for i in V)
    return summa

print(sum_prod(np.array([[1,9,2], [3, 2, 1], [9, 2, 3]]), np.array([[[1], [2], [3]]])))


# %% [markdown]
# <h1>Задача 2. Дана матрица M, напишите функцию, которая бинаризует матрицу по некоторому threshold (то есть, все значения большие threshold становятся равными 1, иначе 0). Напишите тесты для кода

# %%
def binarize(M, threshold=2):
    if M.dtype != int:
        return "Неправильная матрица"
    size = M.shape
    for height in range(0,size[0]):
        for width in range(0,size[1]):
            if M[height, width] > threshold:
                M[height, width] = 1
            else:
                M[height, width] = 0
    return M

print(binarize(np.array([[1,2,3],[3,2,1]])))
print()
print(binarize(np.array([["а","ьб","б"],["г","2","1"]])))
print()
print(binarize(np.array([[7,2,3],[3,2,1],[3,1,7]])))



# %% [markdown]
# <h1>Задача 3. Напишите функцию, которая возвращает уникальные элементы из каждой строки матрицы. Напишите такую же функцию, но для столбцов. Напишите тесты для кода

# %%
def unique_rows(mat):
    finalResult = []
    for row in mat:
        result = []
        for num in row:
            if num in result:
                continue
            else:
                result.append(num)
        finalResult.append(result)
    return finalResult

def unique_columns(mat):
    finalResult = []
    size = mat.shape
    for x in range(0, size[1]):
        result =[]
        for y in range(0, size[0]):
            if mat[y,x] in result:
                continue
            else:
                result.append(mat[y,x])
        finalResult.append(result)
    return finalResult

print(unique_rows(np.array([[1, 2, 3, 3], [4, 4, 5, 6]])))
print(unique_columns(np.array([[1, 2, 3, 3], [4, 4, 5, 6], [1, 2, 3, 3],[5, 2, 6, 7]])))

# %% [markdown]
# <h1>Задача 4. Напишите функцию, которая заполняет матрицу с размерами $(m, n)$ случайными числами, распределенными по нормальному закону. Затем считает мат. ожидание и дисперсию для каждого из столбцов и строк, а также строит для каждой строки и столбца гистограмму значений (использовать функцию hist из модуля matplotlib.plot)

# %%
# Your code goes here

# %% [markdown]
# <h1>Задача 5. Напишите функцию, которая заполняет матрицу $(m, n)$ в шахматном порядке заданными числами $a$ и $b$. Напишите тесты для кода

# %%
def chess(m, n, a, b):
    """"" Проверка на тип данных """""
    if (type(m) != int) or (type(n) != int) or (type(a) != int) or (type(b) != int): 
        return "Неправильные условия"
    """"" Проверка на размер """""
    if m < 0 or n < 0:
        return "Неправильный размер" 
    matrix = np.zeros((m, n))
    counter=0
    for height in range(0,m):
        for width in range(0,n):
            if counter % 2 == 0:
                matrix[height, width] = a
            else:
                matrix[height, width] = b
            counter += 1
    return matrix

print(chess(2,3,1,2))
print()
print(chess(5,5,1,2))
print()
print(chess(-5,5,1,2))
print()
print(chess("a",5,1,2))

# %% [markdown]
# <h1>Задача 6. Напишите функцию, которая отрисовывает прямоугольник с заданными размерами (a, b) на изображении размера (m, n), цвет фона задайте в схеме RGB, как и цвет прямоугольника. Цвета также должны быть параметрами функции. Напишите аналогичную функцию но для овала с полуосями a и b. Напишите тесты для кода.
# Примечание: уравнение эллипса (границы овала) можно записать как:
# <h1>$\frac{(x-x_0)^2}{a^2}+\frac{(y-y_0)^2}{b^2}=1$

# %%
def draw_rectangle(a, b, m, n, rectangle_color, background_color):
    # Your code goes here
    pass

def draw_ellipse(a, b, m, n, ellipse_color, background_color):
    # Your code goes here
    pass

# %% [markdown]
# <h1>Задача 7. Дан некий временной ряд. Для данного ряда нужно найти его: математическое ожидание, дисперсию, СКО, найти все локальные максимумы и минимумы (локальный максимум - это точка, которая больше своих соседних точек, а локальный минимум - это точка, которая меньше своих соседей), а также вычислить для данного ряда другой ряд, получаемый методом скользящего среднего с размером окна $p$.
# <h1>Примечание: метод скользящего среднего подразумевает нахождение среднего из подмножетсва ряда размером $p$

# %%
# Your code goes here

# %% [markdown]
# <h1> Задача 8. Дан некоторый вектор с целочисленными метками классов, напишите функцию, которая выполняет one-hot-encoding для данного вектора
# <h1> One-hot-encoding - представление, в котором на месте метки некоторого класса стоит 1, в остальных позициях стоит 0. Например для вектора [0, 2, 3, 0] one-hot-encoding выглядит как: [[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]

# %%
# Your code goes here


