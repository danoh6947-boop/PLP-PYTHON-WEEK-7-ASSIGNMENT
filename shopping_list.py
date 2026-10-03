shopping_list = []

while True:
    choice = input("Choose add / remove / show / done: ").lower()

    if choice == "add":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print("Item added.")

    elif choice == "remove":
        item = input("Enter the item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Shopping list:")
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Please choose add, remove, show, or done.")