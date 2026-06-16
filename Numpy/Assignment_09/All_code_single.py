import numpy as np

# ==================================================
# TASK 1: Array Creation and Properties
# ==================================================

print("\n===== TASK 1 =====")

# A 1D array of integers from 1 to 10
A = np.arange(1, 11)

# A 2D array of shape (3,3) with values from 1 to 9
B = np.arange(1, 10).reshape(3, 3)

# A NumPy array from list
C = np.array([10, 20, 30, 40, 50])

print("Array A:", A)
print("Shape:", A.shape)
print("Data Type:", A.dtype)

print("\nArray B:")
print(B)
print("Shape:", B.shape)
print("Data Type:", B.dtype)

print("\nArray C:", C)
print("Shape:", C.shape)
print("Data Type:", C.dtype)

# ==================================================
# TASK 2: Array Arithmetic Operations
# ==================================================

print("\n===== TASK 2 =====")

A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("Addition (A+B):", np.add(A, B))
print("Subtraction (A-B):", np.subtract(A, B))
print("Multiplication (A*B):", np.multiply(A, B))
print("Division (A/B):", np.divide(A, B))
print("Power (A**2):", np.power(A, 2))

# ==================================================
# TASK 3: Mathematical Functions
# ==================================================

print("\n===== TASK 3 =====")

values = np.array([4, 6, 8, 10])

# Square root of each element
print("Square Root:", np.sqrt(values))

# Exponential of each element
print("Exponential:", np.exp(values))

# Natural logarithm
print("Natural Logarithm:", np.log(values))

# Sum of all elements
print("Sum:", np.sum(values))

# Cumulative sum
print("Cumulative Sum:", np.cumsum(values))

# ==================================================
# TASK 4: 2D Array Analysis
# ==================================================

print("\n===== TASK 4 =====")

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Row-wise sum
print("Row-wise Sum:", np.sum(data, axis=1))

# Column-wise sum
print("Column-wise Sum:", np.sum(data, axis=0))

# Minimum value
print("Minimum Value:", np.min(data))

# Maximum value
print("Maximum Value:", np.max(data))

# Overall mean
print("Overall Mean:", np.mean(data))

# ==================================================
# TASK 5: Statistical Analysis
# ==================================================

print("\n===== TASK 5 =====")

marks = np.array([85, 90, 66, 72, 88, 95, 60])

# Mean
print("Mean:", np.mean(marks))

# Median
print("Median:", np.median(marks))

# Variance
print("Variance:", np.var(marks))

# Standard Deviation
print("Standard Deviation:", np.std(marks))

# Minimum and Maximum
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

# Range
print("Range:", np.max(marks) - np.min(marks))

# ==================================================
# TASK 6: Sorting and Percentiles
# ==================================================

print("\n===== TASK 6 =====")

marks = np.array([85, 90, 66, 72, 88, 95, 60])

# Sort the array
sorted_marks = np.sort(marks)
print("Sorted Marks:", sorted_marks)

# Percentiles
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))

# Average marks
average_marks = np.mean(marks)
print("Average Marks:", average_marks)

# Count students scoring above average
count_above_average = np.sum(marks > average_marks)
print("Students Above Average:", count_above_average)

# ==================================================
# TASK 7: Sales Data Analysis
# ==================================================

print("\n===== TASK 7 =====")

sales = np.array([1500, 900, 2000, 1800, 1700, 1600])

# Total sales
print("Total Sales:", np.sum(sales))

# Average sales
average_sales = np.mean(sales)
print("Average Daily Sales:", average_sales)

# Highest and lowest sales
highest_day = np.argmax(sales) + 1
lowest_day = np.argmin(sales) + 1

print("Highest Sales:", np.max(sales), "on Day", highest_day)
print("Lowest Sales:", np.min(sales), "on Day", lowest_day)

# Standard deviation
print("Standard Deviation:", np.std(sales))

# Days with sales above average
above_average_days = np.where(sales > average_sales)[0] + 1
print("Days with Sales Above Average:", above_average_days)