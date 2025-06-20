
def busqueda_lineal(list, objetivo):
    for i in range(len(list)):
        if list[i] == objetivo:
            return i
    return -1


def busqueda_binaria(list, objetivo):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == objetivo:
            return mid
        elif list[mid] < objetivo:
            left= mid + 1
        else:
            right= mid - 1
    return -1