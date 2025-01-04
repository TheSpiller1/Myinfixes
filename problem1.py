import shankar_list


def middle_num(linked_list):
    root = linked_list.root

    size = linked_list.size
    first_number = size/2

    count = 0

    while count < first_number - 1:

        root = root.get_prev()
        count += 1

    if size % 2 == 0:
        prev = root.get_prev()
        return [root.get_data(), prev.get_data()]

    else:
        return root.get_data()
