def list_operations():
    my_list = []

    while True:
        print("\nList Operations Menu:")
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. Find Element")
        print("4. Display List")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':  
            element = input("Enter element to insert: ")
            my_list.append(element)
            print(f"{element} inserted into list.")

        elif choice == '2':  
            element = input("Enter element to delete: ")
            if element in my_list:
                my_list.remove(element)
                print(f"{element} removed from list.")
            else:
                print(f"{element} not found in list.")

        elif choice == '3':  
            element = input("Enter element to find: ")
            if element in my_list:
                print(f"{element} is present in the list.")
            else:
                print(f"{element} is not in the list.")

        elif choice == '4':  
            print("Current List:", my_list)

        elif choice == '5':  
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

list_operations()
