# File Handling Assignment

## Overview
This assignment demonstrates Python file handling concepts such as:
- Writing files
- Reading files
- Appending data
- File statistics
- User input handling
- Safe file reading
- Mini project using file export

---

## Task 1: Write Sales Records to a File

### Objective
Write sales data into a text file and read it back.

### Features
- Creates a list of sales
- Writes each sale to `sales_data.txt`
- Reads and prints file contents
- Extra: Saves comma-separated data

### Example Output
1200
450
980
1500
3000

---

## Task 2: Read File in Different Ways

### Objective
Practice different file reading methods.

### Methods Used
- `.read()`
- `.readline()`
- `.readlines()`

### Features
- Reads entire file
- Reads first line
- Converts file lines into integer list

### Example Output
Full File Content:
1200
450
980
1500
3000

First Line:
1200

Sales List:
[1200, 450, 980, 1500, 3000]

---

## Task 3: Append New Sales

### Objective
Append new sales records to an existing file.

### Features
- Adds:
  - 5000
  - 2500
  - 1700
- Prints updated file
- Counts total number of lines

### Example Output
Total Lines: 8

---

## Task 4: Generate Summary Report

### Objective
Calculate statistics from sales data.

### Calculations
- Total Sales
- Highest Sale
- Lowest Sale
- Average Sale

### Example Output
Total Sales: 15330
Highest Sale: 5000
Lowest Sale: 450
Average Sale: 1916.25

---

## Task 5: Create Product Info File

### Objective
Store product information entered by the user.

### Features
- Takes 3 product names and prices
- Saves to `products.txt`
- Reads and displays saved products

### File Format
ProductName | Price

### Example
Mouse | 500
Keyboard | 800
Monitor | 7000

---

## Task 6: Read File Safely

### Objective
Safely read a file only if it exists.

### Method Used
`os.path.exists()`

### Features
- Checks file existence
- Reads content if file exists
- Shows error message if file does not exist

### Example Error
File not found. Please check the filename.

---

## Task 7: Mini Project - Export Discounted Prices

### Objective
Generate a discount report from product prices.

### Features
- Takes discount percentage from user
- Calculates discounted prices
- Saves report to `discount_report.txt`
- Includes summary

### Report Format
Product | Original Price | Discounted Price

### Summary Includes
- Total Items
- Average Discounted Price

---

## How to Run

1. Save the Python file:
   assignment.py

2. Open terminal or command prompt.

3. Run the file:

```bash
python assignment.py