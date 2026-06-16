# Build a simple price calculator app that:
# 1. Takes products price (number input)
# 2. Takes discount percentage (slider from 0 to 50%)
# 3. On button click calculates discounted price
# 4. Shows result using st.success()
# Example:
# Original price : 1000
# Discount: 10%
# Final Price:900
# Extra(optional): show comparison in small table:
# before | After
# (Use st.table() with a simple list of lists).



import streamlit as st

# Title
st.title("Price Calculator App")

# Product price input
price = st.number_input("Enter Product Price", min_value=0.0, value=1000.0)

# Discount slider
discount = st.slider("Select Discount Percentage", 0, 50, 10)

# Button click
if st.button("Calculate Price"):
    # Calculate discounted price
    final_price = price - (price * discount / 100)

    # Show result
    st.success(f"Original Price: ₹{price}")
    st.success(f"Discount: {discount}%")
    st.success(f"Final Price: ₹{final_price:.2f}")

    # Optional comparison table
    st.write("### Price Comparison")
    table_data = [
        ["Before", "After"],
        [price, final_price]
    ]

    st.table(table_data)