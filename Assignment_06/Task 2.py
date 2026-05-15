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