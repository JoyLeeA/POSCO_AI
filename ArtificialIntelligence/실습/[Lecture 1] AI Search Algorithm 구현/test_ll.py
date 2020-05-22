#20200518 Monday

import util

ll = util.LinkedList.create_list(5, 4, 3, 2, 1) # 5-> 4 -> 3 -> 2 -> 1
print(ll)
print(ll.value)  # head's value (헤드 출력)

ll2 = ll.construct(6)  # constructtruct a new list with a value 6
print(ll2) # 6 -> 5-> 4 -> 3 -> 2 -> 1

ll3 = ll.tail  # extract a sub-list that doesn't contain the head
print(ll3) #가장 앞애 있는 값 제거

ll4 = ll3.construct(7)
print(ll4)

print(ll.tail is ll4.tail is ll2.tail.tail)  # linked lists share the sub-list
# is 는 ==과 비슷하다. class 는 object로 정의 되기 때문에 비교 할때 is 사용
# ll.tail이 가지고 있는 object와 114.tail이 가지고 있는 object와 바교하는 것임.

