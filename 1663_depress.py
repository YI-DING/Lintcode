def depress(self, m, k, arr):
    arr.sort()
    result = sum(arr[:k])
    return 'no' if result >= m else 'yes'