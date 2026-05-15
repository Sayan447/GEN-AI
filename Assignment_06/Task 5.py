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