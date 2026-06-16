# Create a samll dashboard with:
# 1. title + description
# "simple sales dashboard"
# 2. A selectbox with months:
# months = ['january' , 'february' ,'march' , 'April]

# 3. A static dictionary of monthly sales:
# sales = {
    # 'january':1200,
    # 'february':1500,
    # 'March':900,
    # 'April':2000,
    
# }


# 4. Display selected month's sales using:
# st.metric() OR st.write()
# 5. Display a bar chart using:
# st.bar_chart(list(slaes.values()))
# (No pandas required -- simple list is allowed.)



import streamlit as st

# Title + Description
st.title("Simple Sales Dashboard")
st.write("This dashboard shows monthly sales data.")

# Months list
months = ['January', 'February', 'March', 'April']

# Sales dictionary
sales = {
    'January': 1200,
    'February': 1500,
    'March': 900,
    'April': 2000,
}

# Selectbox for months
selected_month = st.selectbox("Select a Month", months)

# Display selected month's sales
st.metric(
    label=f"{selected_month} Sales",
    value=f"₹{sales[selected_month]}"
)

# Bar Chart
st.write("### Monthly Sales Chart")
st.bar_chart(list(sales.values()))