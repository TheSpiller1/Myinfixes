import shankar_list

linked_list = shankar_list.ShankarLinkedLists()
adding = input("""
Which numbers do you want to add? """)
while adding.lower() != 'n':
    linked_list.add(int(adding), True)
    adding = input("Which numbers do you want to add? ")

delete = input("""
Which numbers do you want to delete? """)
while delete.lower() != 'n':
    linked_list.delete(int(delete), True)
    delete = input("Which numbers do you want to delete? ")
root = linked_list.root
size = linked_list.size
num = int(input("Give me a number "))
if num == 1:
    print(linked_list.access_list())
counter = 0
times = 0
for every_num in range(size - 1):
    if (size - counter) % num == 0:
        linked_list.delete(root.get_data(), prin=False)
    root = root.get_prev()
    counter += 1

print(linked_list.access_list())
