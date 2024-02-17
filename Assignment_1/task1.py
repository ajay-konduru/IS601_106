# Task 1 (50 points)

# Question 1
arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 1
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48] # 2
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9] # 3

# only output the odd values from the above lists (print the output for all lists)
def odd_values(num, arr):
    print(f'output for arr{num}:')
    for value in arr:
        if value % 2 != 0:
            print(value, end=' ')
    print('\nEnd of odd values\n')

# Testing Question 1
odd_values(1, arr1)
odd_values(2, arr2)
odd_values(3, arr3)

# Question 2
arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # 1
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20] #2
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44] #3

# Only output the sum/total of the lists values (print the output for all lists)
def sum_values(num, arr):
    total = sum(arr)
    print(f'output for arr{num}: {total}\nEnd of sum values\n')

sum_values(1,arr1)
sum_values(2,arr2)
sum_values(3,arr3)

# Question 3
arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100] #1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233] #2 
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33] #3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99] #4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30] #5

# Convert the negative values in the following lists to positive and ouput the sum of all values (print the output for all lists).
def converted_sum_values(num, arr):
    total = sum(abs(value) for value in arr)
    print(f'output for arr{num}: {total}\nEnd of converted sum values\n')
converted_sum_values(1, arr1)
converted_sum_values(2, arr2)
converted_sum_values(3, arr3)   
converted_sum_values(4, arr4)
converted_sum_values(5, arr5)



# Question 4
arr1 = ['apple', '', 'banana', '', 'cherry'] #1
arr2 = ['', 'dog', '', 'cat', ''] #2
arr3 = ['hello', '', 'world', '', ''] #3
arr4 = ['', '', '', '', ''] #4
arr5 = ['one', '', 'two', '', 'three'] #5
# Remove empty strings from the above lists and output the lists (print the output for all lists)
def empty_str(num, arr):
    filtered_arr = [value for value in arr if value != '']
    print(f'output for arr{num}: {filtered_arr}\nEnd of empty str values\n')

empty_str(1, arr1)
empty_str(2, arr2)
empty_str(3, arr3)
empty_str(4, arr4)
empty_str(5, arr5)


# Question 5
arr_q5 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]
# Write a function that takes in a list and prints the smallest value from that list.
def print_smallest_value(arr):
    if arr:
        print(f'The smallest value in the list is: {min(arr)}')
    else:
        print('The list is empty.')

print_smallest_value(arr_q5)
