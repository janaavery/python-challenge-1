# Avemenu dictionary
avemenu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Grapes": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# avemenu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which avemenu category they want to order
    print("From which avemenu would you like to order? ")

    # Create a variable for the avemenu item number
    i = 1
    # Create a dictionary to store the avemenu for later retrieval
    avemenu_items = {}

    # Print the options to choose from avemenu headings (all the first level
    # dictionary items in avemenu).
    for key in avemenu.keys():
        print(f"{i}: {key}")
        # Store the avemenu category associated with its avemenu item number
        avemenu_items[i] = key
        # Add 1 to the avemenu item number
        i += 1

    # Get the customer's input
    avemenu_category = input("Type avemenu number: ")

    # Check if the customer's input is a number
    if avemenu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(avemenu_category) in avemenu_items.keys():
            # Save the avemenu category name to a variable
            avemenu_category_name = avemenu_items[int(avemenu_category)]
            # Print out the avemenu category name they selected
            print(f"You selected {avemenu_category_name}")

            # Print out the avemenu options from the avemenu_category_name
            print(f"What {avemenu_category_name} item would you like to order?")
            i = 1
            avemenu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in avemenu[avemenu_category_name].items():
                # Check if the avemenu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        avemenu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    avemenu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input avemenu item number
            avemenu_item = input("Type avemenu item number: ")

            # 3. Check if the customer typed a number
            if avemenu_item.isdigit():
                # Convert the avemenu selection to an integer
                avemenu_item = int(avemenu_item)

                # 4. Check if the avemenu selection is in the avemenu items
                if avemenu_item in avemenu_items.keys():
                    # Store the item name as a variable
                    item_name = avemenu_items[avemenu_item]["Item name"]

                    # Ask the customer for the quantity of the avemenu item
                    quantity = input(f"How many {item_name} would you like? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():  # isdigit() checks if a string is a number
                        quantity = int(quantity)    # Convert the quantity to an integer    
                    else:   # If the quantity is not a number
                        quantity = 1    # Set the quantity to 1

                        

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": avemenu_items[avemenu_item]["Price"],
                        "Quantity": quantity
                    })                  


                    # Tell the customer that their input isn't valid
                else:
                    print(f"{avemenu_item} was not a avemenu item.")

                # Tell the customer they didn't select a avemenu option

        else:
            # Tell the customer they didn't select a avemenu option
            print(f"{avemenu_category} was not a avemenu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering.lower() == "n":
                # Keep ordering
                place_order = False
                # Exit the keep ordering question loop
                break
                # Complete the order
                
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order!")
                # Exit the keep ordering question loop
                break

                # Tell the customer to try again
        elif keep_ordering.lower() == "y":  # If the customer wants to keep ordering
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)

    # 9. Create space strings
    item_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item['Price']} | {item['Quantity']}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print(f"\nTotal: ${sum([item['Price'] * item['Quantity'] for item in order])}")