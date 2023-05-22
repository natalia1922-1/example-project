# find_max
# sum_of.list
# n!
# fun sum l
# is empty?
#    y -> 0
#    n -> l(0) + sum(reszta)
#fibbonacci
# sudoku od 1 - 4

def sumList(listToSum):
    y = 0

    if len(listToSum) == 0:
        return y

    for number in listToSum:
        y = number + y

    return y


list = [1, 2, 3]

print(sumList(list))