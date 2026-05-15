
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
