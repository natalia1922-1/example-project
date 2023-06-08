# find_max
# sum_of.list
# n!
# fibbonacci
# sudoku od 1-4

# fun find_max l
# length of l is l?
#   y -> l(0)
# max = find_max(l(1:end))
# max is greater than l(0)?
# y -> max
# else y -> l(0)

def find_max(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        tmp_max = find_max(lista[1:])
        if tmp_max > lista[0]:
            return tmp_max
        else:
            return lista[0]


# fun fibonacci n
# n == 0?
#   y -> 0
# n == 1?
#   y ->
# y -> fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# fun sum l
# is empty?
# y -> 0
# y -> l(0) + sum(reszta)

def sumList(listToSum):
    if len(listToSum) == 0:
        return 0
    else:
        return listToSum[0] + sumList(listToSum[1:])


# fun n_silnia n
# n == 0?
#   y -> 1
# n == 1?
#   y -> 1
# y -> n * n_silnia(n-1)

def n_silnia(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * n_silnia(n - 1)


###############################
lista = [1, 2, 3, 4, 5]
print(f'sumList({lista}) = {sumList(lista)}')
###############################
n = 4
print(f'{n}! = {n_silnia(n)}')
###############################
n = 7
print(f'fibonacci({n}) = {fibonacci(n)}')
###############################
lista = [1, 5, 3, 2, -1]
print(f'find_max({lista}) = {find_max(lista)}')
