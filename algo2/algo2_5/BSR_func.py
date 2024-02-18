def GenerateBBSTArray(unsorted_array):
    if len(unsorted_array) == 1:
        return unsorted_array
    sorted_array = sorted(unsorted_array)
    size = len(sorted_array)
    bbst_array = []
    index = step = int((size - 1) / 2)  # середина массива
    while len(bbst_array) < size:
        base = index
        while index < size:
            bbst_array.append(sorted_array[index])
            index += step + 1  # +1 из-за того, что в python нумерация индексов с 0
        index = int((base-1)/2)
        step = base
    return bbst_array
