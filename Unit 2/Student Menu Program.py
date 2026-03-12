students = {}

while True:
    print("\n1.Add 2.Search 3.List 4.Update 5.Delete 6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll: ")
        name = input("Name: ")
        students[roll] = name

    elif choice == "2":
        roll = input("Roll: ")
        print(students.get(roll, "Not found"))

    elif choice == "3":
        print(students)

    elif choice == "4":
        roll = input("Roll: ")
        if roll in students:
            students[roll] = input("New Name: ")

    elif choice == "5":
        roll = input("Roll: ")
        students.pop(roll, None)

    elif choice == "6":
        break
