# Python Functions Assignment

## Task 1 - apply_discount()
Created a function that:
- Applies discount on price
- Uses default discount of 5%
- Caps discount at 60%

Example:
apply_discount(1000, 10) → 900
apply_discount(500) → 475


## Task 2 - factorial()
Created a recursive factorial function:
- Handles n == 0 and n == 1
- Prints error for negative numbers

Example:
factorial(5) → 120
factorial(0) → 1
factorial(-3) → Error


## Task 3 - Lambda Function (GST)
Created lambda function for 18% GST.

Example:
gst(100) → 118


## Task 4 - map()
Applied GST to a list using map().

Example:
[100,250,400] → [118,295,472]


## Task 5 - filter()
Filtered:
- Prices > 500
- Prices <= 500


## Task 6 - process_prices()
Combined:
- map() for 10% discount
- filter() for prices above 300


## Task 7 - Menu System
Built an interactive menu:
1. Add price
2. Show average price
3. Show highest price
q. Quit