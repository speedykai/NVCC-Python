# PURPOSE: Process information from a ".txt" file and convert into
# a grocery list with proper formatting.
# Author: Kaivan Taylor
# Date: 11/07/17

# Step 1 - Create a dictionary for grocery list name, price, and unit

grocery_price = open("grocery_price_list.txt", "r") # Open up the .txt file with read function.
grocery_price_dic = {}  # Create new dictionary for grocery prices an units.

for line in grocery_price:
    format_dic = line.strip()
    format_dic = line.split()   # Obtain .txt information and format into usable data.
    print(format_dic)
    
    item_name = str(format_dic[0])
    item_price = (float(format_dic[1]))
    item_unit = str(format_dic[2])  # Declare data type for each index and assign a variable.

    grocery_price_dic[item_name] = item_price,item_unit # Convert new variables to new dictionary.

grocery_price.close() # Close the .txt file.

# Step 2 - Read file from a grocery list

grocery_list = open("grocery_user_test.txt", "r") # Open the .txt file with read function.
total_cost = 0 # Set a variable for calculating total cost. By default, the value is 0 for no items purchased.
counter = 0 # Set counter to zero for the for loop in order to number each item (i.e. 1.,2.,3.).

print("Cash Register List\n-----------------------------------------------------")  # Title name for the top of the list
print("{:5s}{:5s}     {:11s}{:10s}{:12s}{:2s}".format("N(#)","Qty","Item","Unit","Unit Price","Extension")) # Format to match listed items

for line in grocery_list:
    format_user = line.strip()
    format_user = line.split()  # Obtain .txt information and format into usable data.
    #print(format_user)
    
    quantity = int(format_user[0])
    food_name = str(format_user[1]) # Declare data type for each index and assign a variable.
    #print(quantity)
    #print(food_name)

    counter += 1 # Numbered list counter adds 1 for ever item and starts with the number 1 for the first item.
    price_extension = grocery_price_dic[food_name]  # Obtain value from dictionary by using "food_name" key.
    unit_price = price_extension[0] # Obtain the unit price by calling index 2 of price_extension tuple.
    unit = price_extension[1] # Obtain unit by calling index 1 of price_extension tuple.
    extension = unit_price*quantity # Calculate the extension by multiplying unit price and quantity.

    print("{:2d}. {:4d}  {:10s} {:10s}{:3}        {:.2f}".format(counter,quantity,food_name,unit,unit_price,extension)) # Format to match header.

    total_cost = float(total_cost + extension) # Add the total of calculated extension cost for each item.

print("{:15s}{:.2f}".format("\nThe total of all items: ",total_cost)) # Print the total of all items to user.
print("-----------------------------------------------------") # Lines for neatness and visibility.

#input("Press Enter to exit") # Prevents the program from automatically closing when running .py program.

