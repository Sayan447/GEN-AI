# =====================================================
# TASK 1: Division Program with Exception Handling
# =====================================================

print("===== TASK 1: Division Program =====")

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Denominator cannot be 0.")

else:
    print("Result =", result)

finally:
    print("Operation Complete")


print("\n" + "=" * 50)


# =====================================================
# TASK 2: Bill Calculator with Error Handling
# =====================================================

print("===== TASK 2: Bill Calculator =====")

prices = [100, 250, -50, "abc", 300, 450.5, None]

total = 0

for price in prices:
    try:
        # Check if price is a number
        if not isinstance(price, (int, float)):
            raise TypeError("Value is not a number")

        # Raise custom ValueError for negative prices
        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price

        print(f"Added: {price}")
        print(f"Running Total = {total}")

    except TypeError as e:
        print("TypeError:", e)

    except ValueError as e:
        print("ValueError:", e)

print("Final Total =", total)

print("\n" + "=" * 50)


# =====================================================
# TASK 3: Age Validator
# =====================================================

print("===== TASK 3: Age Validator =====")


def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")


try:
    age = int(input("Enter your age: "))

    check_age(age)

    print("Valid Age")

except ValueError as e:
    print("Error:", e)

print("\n" + "=" * 50)


# =====================================================
# TASK 4: File Reader with Exception Handling
# =====================================================

print("===== TASK 4: File Reader =====")

try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:

        print("\nFirst 3 lines of the file:\n")

        for i in range(3):
            line = file.readline()

            if not line:
                break

            print(line.strip())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("File operation attempted")

print("\n" + "=" * 50)


# =====================================================
# TASK 5: Mini Program - Safe Shopping Cart
# =====================================================

print("===== TASK 5: Safe Shopping Cart =====")


# Custom Exception Class
class NegativePriceError(Exception):
    pass


cart = []

while True:
    try:
        price = input("Enter product price (or 'q' to quit): ")

        # Stop loop if user enters q
        if price.lower() == 'q':
            break

        # Convert input into float
        price = float(price)

        # Raise custom exception
        if price < 0:
            raise NegativePriceError(
                "Negative price is not allowed"
            )

        # Add valid price to cart
        cart.append(price)

        print("Item added successfully!")

    except ValueError:
        print("Error: Please enter a valid number.")

    except NegativePriceError as e:
        print("Error:", e)

# Final summary
print("\n===== Shopping Summary =====")
print("Total Items =", len(cart))
print("Total Bill =", sum(cart))