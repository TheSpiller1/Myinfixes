import shankar_list


def rotation(n):
    linked_list = shankar_list.ShankarLinkedLists()
    adding = input("""
Which numbers do you want to add? """)
    while adding.lower() != 'n':
        linked_list.add(int(adding))
        adding = input("Which numbers do you want to add? ")

    delete = input("""
Which numbers do you want to delete? """)
    while delete.lower() != 'n':
        linked_list.delete(int(delete), True)
        delete = input("Which numbers do you want to delete? ")

    root = linked_list.root
    changing_root = linked_list.root
    if linked_list.size <= n:
        return "Invalid rotation size"
    for every_num in range(n):
        changing_root = changing_root.get_prev()
    before_root = changing_root.get_prev()
    linked_list.delete(root.get_data(), False)
    changing_root.set_prev(root)
    root.set_prev(before_root)
    linked_list.print_list(3, root.get_data(), True, n)


rotation(2)
