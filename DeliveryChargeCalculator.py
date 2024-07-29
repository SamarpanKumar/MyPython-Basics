# Prompt the user to enter the purchase total
purchase_total = float(input("Enter the purchase total: $"))

# Check if the purchase total is above $150
if purchase_total > 150:
    # Prompt the user to enter the number of items
    num_items = int(input("Enter the number of items to be delivered: "))

    # Prompt the user to enter the delivery day
    delivery_day = int(input("Enter the delivery day (1 for same day, 2 for next day): "))

    # Calculate the delivery cost based on the conditions. 
    if num_items <= 5:
        if delivery_day == 1:
            delivery_cost = 8.0
        elif delivery_day == 2:
            delivery_cost = num_items * 1.50
        else:
            print("Invalid delivery day entered!")
            exit(0)
    elif num_items >= 6:
        if delivery_day == 1:
            delivery_cost = num_items * 2.50
        elif delivery_day == 2:
            delivery_cost = num_items * 1.20
        else:
            print("Invalid delivery day entered!")
            exit(0)
    else:
        print("Invalid number of items entered!")
        exit(0)

    # Calculate the total cost
    total_cost = purchase_total + delivery_cost

    # Display the delivery cost and total cost to the user
    print("Delivery cost: ${:.2f}".format(delivery_cost))
    print("Total cost: ${:.2f}".format(total_cost))
else:
    print("Purchase total should be above $150!")





