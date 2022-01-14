# 1. Сумма вершин каждой плоскости

n = int(input('Нумерация:\n'))      # То, что нужно пронумеровать, 8 точек, n = 8
list = list(range(n+1))             # Разложение в список цифр от 0 до 8, нужны будут для подсчета
numbers = list[1:]                  # Срез для цифр от 1 до 8
def count(num):
    part1 = (numbers[0] + numbers[7] + numbers[1] + numbers[6])         # Пары цифр 1-8, 2-7
    part2 = (numbers[2] + numbers[5] + numbers[3] + numbers[4])         # Пары цифр 3-6, 4-5
    if part1 == part2:
        return part1

print(count(numbers))

# 2. Сколько вариантов расположения цифр может быть, если не принимать во внимание вращение кубика в пространстве?

points = 4      # количество точек, 2 пары, которые можем менять
facets = 6      # количество пар цифр взятых из сторон куба
options = points * facets
print(options)
