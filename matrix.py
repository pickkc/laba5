import random

size = int(input("Введите размер: "))

matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    matrix.append(row)

for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j] = matrix[j][i] = random.randint(0, 1)

for row in matrix:
    print(row)

izol = []
end = []
dom = []

for i in range(size):
    a = sum(matrix[i])
    if a == 0:
        izol.append(i)
    elif a == 1:
        end.append(i)
    elif a == size - 1:
        dom.append(i)

if not izol:
    izol.append("Неть")
if not end:
    end.append("Неть")
if not dom:
    dom.append("Неть")

graphs = 0
for i in range(size):
    for j in range(size):
        graphs += matrix[i][j]
graphs = graphs // 2
inc = [[0] * graphs for _ in range (size)]
idx = 0
for j in range(size):
    for i in range(j + 1, size):
        if matrix[i][j] == 1:
            inc[i][idx] = 1
            inc[j][idx] = 1
            idx += 1

izol1 = []
end1 = []
dom1 = []

for i in range(size):
    c = sum(inc[i])
    if c == 0:
        izol1.append(i)
    elif c == 1:
        end1.append(i)
    elif c == size - 1:
        dom1.append(i)

if not izol1:
    izol1.append("Неть")
if not end1:
    end1.append("Неть")
if not dom1:
    dom1.append("Неть")

print("Изолированные вершины: ", izol)
print("Концевые вершины: ", end)
print("Доминирующие вершины: ", dom)
print("Размер графа: ", graphs)
print("Матрица инцидентности:")
for b in range(size):
    print(inc[b])
print("Изолированные вершины: ", izol1)
print("Концевые вершины: ", end1)
print("Доминирующие вершины: ", dom1)


