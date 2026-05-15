# Method 1
# import math_utils

# # Method 2
# from math_utils import square

# print("Addition:", math_utils.add(5, 3))
# print("Subtraction:", math_utils.subtract(10, 4))
# print("Square:", square(6))


# ---------------------------------------
# import string_utils

# text = "python modules are easy"

# print("Capitalized:", string_utils.capitalize_words(text))
# print("Reversed:", string_utils.reverse_string(text))
# print("Word Count:", string_utils.word_count(text))




# -----------------------------------------
# Import from package
# from shop_package.discount import apply_discount, flat_discount
# from shop_package.billing import calculate_total, apply_tax


# # Testing discount functions
# price = 1000

# print("Discounted Price:", apply_discount(price, 10))
# print("Flat Discount Price:", flat_discount(price))


# # Testing billing functions
# total = calculate_total(500, 300)
# print("Total Bill:", total)

# final_amount = apply_tax(total)
# print("Final Amount with Tax:", final_amount)




# --------------------------------------------------
# Import package module with alias
import shop_package.discount as disc

# Import specific function
from shop_package.billing import calculate_total, apply_tax


# Calling discount functions
print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))


# Calling billing functions
prices = [100, 200, 300]

total = calculate_total(prices)
print(total)

print(apply_tax(total))