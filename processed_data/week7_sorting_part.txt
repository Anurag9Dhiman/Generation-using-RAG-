# week7_sorting_part.py

from abc import ABC, abstractmethod

# --- Abstraction for sorting algorithms ---
class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, data):
        pass


# --- Concrete sorting algorithms ---
class InsertionSort(SortingAlgorithm):
    def sort(self, data):
        arr = list(data)  # copy to avoid mutating external
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


class SelectionSort(SortingAlgorithm):
    def sort(self, data):
        arr = list(data)
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr


# --- Context / Orchestrator ---
class SortContext:
    def __init__(self, algorithm: SortingAlgorithm):
        self.algorithm = algorithm

    def execute(self, data):
        return self.algorithm.sort(data)


if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    ctx = SortContext(InsertionSort())
    print("Insertion Sort:", ctx.execute(arr))

    ctx = SortContext(SelectionSort())
    print("Selection Sort:", ctx.execute(arr))
