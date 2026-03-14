#	Write a program that:
#	Has a predefined dictionary of groceries with prices.
#	Lets the user "add" items by typing their names.
#	For each valid item, asks for the quantity.
#	Keeps adding to the cart until the user types "checkout".
#	Displays a final bill: each item, quantity, subtotal, and total.


# Predefined dictionary of groceries with prices

groceries = {"milk": 3.00, "bread": 4.00, "banana": 2.50}
cart = {}     # Empty dictionary for the shopping cart

print("Welcome to grocery store!")
print("Available items and prices")

for item, price in groceries.items():
    print(item, ":", "$", price)

# loop to allow user to add items
while True:
    item = input("\nEnter item name (or type 'checkout'): ").lower()

    if item == "checkout":
        break
    if item in groceries:
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
    else:
        print("Item not Available.")


# Display final bill
print("\nFinal Bill")
print("----------------------")

total = 0

for item, quantity in cart.items():
    price = groceries[item]
    subtotal = price * quantity
    total += subtotal
    print(f"{item} x {quantity} = ${subtotal:.2f}")

print("----------------------")
print(f"Total = ${total:.2f}")
