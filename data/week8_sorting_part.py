# week8_sorting_part.py

from week7_sorting_part import SortingAlgorithm, SortContext


# --- Merge Sort Implementation ---
class MergeSort(SortingAlgorithm):
    def sort(self, data):
        arr = list(data)
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


# --- Quick Sort Implementation ---
class QuickSort(SortingAlgorithm):
    def sort(self, data):
        arr = list(data)
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort(self, arr, low, high):
        if low < high:
            p = self._partition(arr, low, high)
            self._quick_sort(arr, low, p - 1)
            self._quick_sort(arr, p + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


if __name__ == "__main__":
    data = [9, 4, 7, 3, 1, 5, 2]
    ctx = SortContext(MergeSort())
    print("Merge Sort:", ctx.execute(data))

    ctx = SortContext(QuickSort())
    print("Quick Sort:", ctx.execute(data))
