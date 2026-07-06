# receipt.py
# Mini project: ASCII Receipt Printer (see README.md for the brief)

STORE_NAME = "THE CORNER STORE"

item_1_name = "Coffee"
item_1_price = 3.50
item_2_name = "Muffin"
item_2_price = 2.25

tax_rate = 0.08

# TODO: compute subtotal, tax, and total from the variables above
subtotal = item_1_price + item_2_price
tax = subtotal * tax_rate
total = subtotal + tax

# TODO: print a formatted receipt using what you know so far
# (variables, print() with sep/end, comments). Perfect alignment isn't
# required yet - that comes with string formatting later.
print("=" * 22)
print(STORE_NAME.center(22))
print("=" * 22)
print(item_1_name, item_1_price)
print(item_2_name, item_2_price)
print("-" * 22)
print("Subtotal", round(subtotal, 2))
print("Tax", round(tax, 2))
print("Total", round(total, 2))
print("=" * 22)
