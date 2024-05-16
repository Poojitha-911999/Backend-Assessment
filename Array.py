def unique_values(arr):
    unique_arr = []
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)
    return unique_arr

input_arr = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8]
print(unique_values(input_arr)) 
