# A
list1 = list([1, 2, 3, 4, 5, 'apple', 'pineapple', 'banana', 'cherry'])
print(list1)
# B+C
list2 = list1.copy()
list2.append(66)
print(list2)
# D
list1.insert(3, 'chocolate')
print(list1)
# E
list3 = [10, 20, 30, 40]
list3.extend(list2)
print(list3)

list4 = [5, 15, 25, 30]
list4 = list1 + list4
print(list4)

# F+G
pop_item = list1.pop(7)
print('Element index .pop: {}'.format(pop_item))
print('New list1 after del index .pop: {}'.format(list1))
list1.remove('cherry')
print('New list1 after .remove cherry: {}'.format(list1))
# H
print('Find element chocolate index : {} '"\n".format(list1.index('chocolate')))

# 5
subset_list = [1, 5, 10, 15, 20, 30, 45, 50, 60, 70, 'chocolate']
print(subset_list[-1][::-1])
print(subset_list[::-1])
print(subset_list[1:6:2])
print(subset_list[-1::])
