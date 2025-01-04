import shankar_list


def enqueue(linked, customer):
    print(f"""
{customer} just entered the line
""")
    linked.add(customer)


def dequeue(linked, root_):
    for every in range(linked.size - 1):
        root_ = root_.get_prev()
    print(f"""
{root_.get_data} has just been dequed.
""")
    linked.delete(root_, True)


linked_list = shankar_list.ShankarLinkedLists()

adding = input("""Name the customers entering your shop. """)
while adding.lower() != 'n':
    enqueue(linked_list, adding)
    adding = input("Name the customers entering your shop. ")

root = linked_list.root
delete = input("""
Which customers do you want to exit the line? """)
while delete.lower() != 'n':
    dequeue(linked_list, root)
    delete = input("Which customers do you want to exit the line?  ")



