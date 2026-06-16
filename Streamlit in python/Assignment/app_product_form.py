# Create a simple from UI:
# 1. Use streamlit sidebar to enter:
    # Product Name
    # Category(selectbox with 3-5 options)
    # price
# 2. When user click "Add Product",show:
    # A success message
    # The product details in clean format

# use components:
# st.sidebar.text_input
# st.sidebar.selectbox
# st.sidebar.number_input
# st.sidebar.button



import streamlit as st

# App Title
st.title("Product Form UI")

# Sidebar Inputs
st.sidebar.header("Enter Product Details")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Books", "Food", "Accessories"]
)

price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    value=100.0
)

# Sidebar Button
if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully!")

    # Display product details
    st.write("## Product Details")
    st.write(f"**Product Name:** {product_name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** ₹{price:.2f}")