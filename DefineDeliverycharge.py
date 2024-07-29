#Making Delivery Charge Calculator by using define!

def calculate_delivery_charges(purchase_total, num_items, delivery_day):
    if purchase_total <= 150:
        print("ERR: Sorry, purchase total needs to be above $150.")
        return None, None

    if num_items <= 5:
        delivery_charges = 8.00
    elif num_items >= 6 and delivery_day == 1:
        delivery_charges = num_items * 1.50
    elif num_items >= 6 and delivery_day == 2:
        delivery_charges = num_items * 2.50
    else:
        print("ERR: Invalid delivery day. Please enter [1] for same day and [2] for next day delivery.")
        return None, None

    total_cost = purchase_total + delivery_charges
    return delivery_charges, total_cost

print("---------------------------------------------------------------------------------")
print(" Welcome to delivery charges Calculator")
print(" ----------------------------------------")

while True:
    purchase_total = float(input("\nPlease enter purchase total: "))
    num_items = int(input("Please enter number of items: "))
    delivery_day = int(input("Please enter delivery day ([1] for same day and [2] for next day delivery): "))

    delivery_charges, total_cost = calculate_delivery_charges(purchase_total, num_items, delivery_day)

    if delivery_charges is not None and total_cost is not None:
        print(f"\nDelivery charges: ${delivery_charges:.2f}")
        print(f"Total cost: ${total_cost:.2f}\n")

    another_purchase = input("Do you want to calculate delivery charges for another purchase? (y/n): ")
    if another_purchase.lower() != 'y':
        print("\nThanks for using the delivery charges Calculator!\nSee you again!")
        break

