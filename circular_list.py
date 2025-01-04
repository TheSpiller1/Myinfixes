import shankar_list
import problem1


def circular_list(ll, rooty):
    original = rooty
    for en in range(ll.size - 1):
        rooty = rooty.get_prev()

    rooty.set_prev(original)
    return f"The linked list is {ll.access_list()}"


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


real = linked_list.root


middle_numbers = problem1.middle_num(linked_list)
new_linked_list = shankar_list.ShankarLinkedLists()
try:
    if len(middle_numbers) == 2:
        while real.get_data() != middle_numbers[1]:
            new_linked_list.add(real.get_data(), False)
            linked_list.delete(real.get_data(), False)
            real = real.get_prev()
except TypeError:
    while real.get_data() != middle_numbers:
        new_linked_list.add(real.get_data(), False)
        linked_list.delete(real.get_data(), False)
        real = real.get_prev()

circular_list(linked_list, real)
main = new_linked_list.root
circular_list(new_linked_list, main)

print(f"The two linked lists are: {linked_list.access_list()} and {new_linked_list.access_list()}")
