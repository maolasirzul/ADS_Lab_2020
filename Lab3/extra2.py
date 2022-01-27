from bigO import BigO

from bigO import BigO

def selectionSort(array):  # in-place, unstable
    '''
    Best : O(n^2) Time | O(1) Space
    Average : O(n^2) Time | O(1) Space
    Worst : O(n^2) Time | O(1) Space
    '''
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        currentIdx += 1
    return array


lib = BigO()
complexity = lib.test(selectionSort, "random")
complexity = lib.test(selectionSort, "sorted")
complexity = lib.test(selectionSort, "reversed")
complexity = lib.test(selectionSort, "partial")
complexity = lib.test(selectionSort, "Ksorted")