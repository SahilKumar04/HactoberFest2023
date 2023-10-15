# Creating an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements in the array
first_element = my_array[0]  # Access the first element (index 0)
second_element = my_array[1]  # Access the second element (index 1)

# Modifying elements in the array
my_array[3] = 10  # Change the fourth element to 10

# Finding the length of the array
array_length = len(my_array)

# Iterating through the array
for element in my_array:
    print(element)

# Adding elements to the end of the array
my_array.append(6)  # Appends 6 to the end of the array

# Removing elements from the array
my_array.remove(3)  # Removes the element with the value 3

# Checking if an element exists in the array
element_exists = 4 in my_array

# Finding the index of an element in the array
index_of_element = my_array.index(5)  # Returns the index of element 5

# Reversing the array
my_array.reverse()

# Sorting the array
my_array.sort()

# Creating a 2D array (an array of arrays)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a 2D array
element = matrix[1][2]  # Accessing the element in the second row and third column

# Adding a new row to the 2D array
new_row = [10, 11, 12]
matrix.append(new_row)
