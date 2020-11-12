float_array = [1.0, 2.2, 3.3, 4.4]
max_index = len(float_array) - 1

min_index = 0

for i in range(len(float_array) // 2):
    temp_value = float_array[max_index]
    float_array[max_index] = float_array[min_index]
    float_array[min_index] = temp_value

    min_index += 1
    max_index -= 1

print(float_array)
