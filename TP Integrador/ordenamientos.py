
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >=0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


def merge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
