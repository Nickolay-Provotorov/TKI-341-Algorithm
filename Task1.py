import random
import time

n = 10000
array = [random.randint(-100, 100) for _ in range(n)]

def bubble_sort(arr):
    arr = arr.copy()
    comparisons = 0

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr, comparisons


def insertion_sort(arr):
    arr = arr.copy()
    comparisons = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons


def quick_sort(arr):
    comparisons = [0]

    def sort(low, high):
        if low < high:
            pivot = arr[(low + high) // 2]
            i = low
            j = high

            while i <= j:
                while True:
                    comparisons[0] += 1
                    if arr[i] < pivot:
                        i += 1
                    else:
                        break

                while True:
                    comparisons[0] += 1
                    if arr[j] > pivot:
                        j -= 1
                    else:
                        break

                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1

            if low < j:
                sort(low, j)

            if i < high:
                sort(i, high)

    sort(0, len(arr) - 1)

    return arr, comparisons[0]


algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Hoare Quick Sort", quick_sort)
]

print("Number of elements:", n)
print()

for name, algorithm in algorithms:
    start = time.perf_counter()
    sorted_array, comparisons = algorithm(array)
    elapsed = time.perf_counter() - start

    print(name)
    print("Number of comparisons:", comparisons)
    print("Execution time:", round(elapsed, 6), "seconds")
    print("Array is sorted:", sorted_array == sorted(array))
