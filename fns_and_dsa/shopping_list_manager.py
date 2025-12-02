"""
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list.
This task focuses on using lists to store and manipulate data dynamically.
"""

#implement functionality

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Prompt for and add an item
            item_name = input("Enter the item to add: ")
            # add items to list
            shopping_list.append(item_name)
            print(f"Item '{item_name}' added to shopping list\n")
            
        elif choice == '2':
            # Prompt for and remove an item
            item_name = input("Enter the item to remove: ")
            #remove item from list
            shopping_list.remove(item_name)
            print(f"Item '{item_name}' removed from shopping list\n")

        elif choice == '3':
            # Display the shopping list
            print(f"'{len(shopping_list)}' availabe in shopping list")
            #display the current list(view items in the list)
            print(shopping_list)
            print()

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    


if __name__ == "__main__":
    main()