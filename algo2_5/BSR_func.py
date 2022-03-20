def GenerateBBSTArray(unsorted_array):
    sorted_array = sorted(unsorted_array)
    bbst_array = [None] * len(sorted_array)
    root_index = int((len(sorted_array) - 1) / 2)  # середина массива
    bbst_array[0] = sorted_array[root_index]
    for i in range(1, root_index+1):
        bbst_array[2*i-1] = sorted_array[root_index-i]
        bbst_array[2*i] = sorted_array[root_index+i]
    return bbst_array
