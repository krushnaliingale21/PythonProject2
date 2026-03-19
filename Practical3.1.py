# students = []
#
# def add_student():
#     sid = input("Enter Student ID: ")
#     name = input("Enter Student Name: ")
#     students.append({"id": sid, "name": name})
#     print("Student added successfully!")
#
# def view_students():
#     if not students:
#         print("No students found.")
#     else:
#         for s in students:
#             print("ID:", s["id"], "| Name:", s["name"])
#
# def update_student():
#     sid = input("Enter ID to update: ")
#     for s in students:
#         if s["id"] == sid:
#             s["name"] = input("Enter new name: ")
#             print("Updated successfully!")
#             return
#     print("Student not found.")
#
# def delete_student():
#     sid = input("Enter ID to delete: ")
#     for s in students:
#         if s["id"] == sid:
#             students.remove(s)
#             print("Deleted successfully!")
#             return
#     print("Student not found.")
#
# def search_student():
#     key = input("Enter ID or Name to search: ")
#     found = False
#     for s in students:
#         if s["id"] == key or s["name"] == key:
#             print("Found -> ID:", s["id"], "| Name:", s["name"])
#             found = True
#     if not found:
#         print("Student not found.")
#
# # Menu
# while True:
#     print("\n1.Add  2.View  3.Update  4.Delete  5.Search  6.Exit")
#     choice = input("Enter choice: ")
#
#     if choice == '1':
#         add_student()
#     elif choice == '2':
#         view_students()
#     elif choice == '3':
#         update_student()
#     elif choice == '4':
#         delete_student()
#     elif choice == '5':
#         search_student()
#     elif choice == '6':
#         break
#     else:
#         print("Invalid choice!")


# # Take input list from user
# items = list(map(int, input("Enter item numbers separated by space: ").split()))
#
# # a) Total number of items
# print("Total items:", len(items))
#
# # b) Last item
# print("Last item:", items[-1])
#
# # c) Sorted list
# sorted_items = sorted(items)
# print("Sorted list:", sorted_items)
#
# # d) Check item 515
# if 515 in items:
#     print("Yes")
# else:
#     print("No")
#
# # e) Add new items and sort
# items.extend([121, 321])
# items.sort()
# print("Updated sorted list:", items)