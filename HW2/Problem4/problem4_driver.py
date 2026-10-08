from problem4 import SortedDoublyLinkedList


lst = SortedDoublyLinkedList()

lst.add(10)
lst.add(4)
lst.add(29)
lst.add(8)
lst.add(2)
lst.add(15)
lst.add(41)

lst.print_list()
print(lst.total())
print(lst.sum_middle_three())
print(lst.median())

lst.delete(41)

lst.print_list()
print(lst.total())
print(lst.sum_middle_three())
print(lst.median())

lst.add(8)

lst.print_list()
print(lst.count(8))
print(lst.count(5))
print(lst.exists(15))
print(lst.exists(5))
