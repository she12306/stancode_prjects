"""
File: add2.py
Name: Heather Ou
------------------------
No data structure.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    # Determine the length of ans
    l1_len = count_linked_list_len(l1)
    l2_len = count_linked_list_len(l2)
    ans_len = max(l1_len, l2_len)

    # First node
    ans = ListNode(0, None)
    ans.val = l1.val + l2.val
    if ans.val >= 10:
        ans.val = ans.val % 10
        carry = 1  # 進位
    else:
        carry = 0
    # Other node
    ans_cur = ans
    l1_cur = l1
    l2_cur = l2
    # 站在當前這個node上，先建立下一個node，再定義他的val。下一輪再移到那個node上，接續建立下一個。
    for i in range(ans_len-1):
        # l1_len, l2_len might be different.
        if l1_cur.next is None:
            l1_cur.next = ListNode(0, None)
        if l2_cur.next is None:
            l2_cur.next = ListNode(0, None)
        # Create next node and assign val of next node
        ans_cur.next = ListNode(0, None)
        ans_cur.next.val = l1_cur.next.val + l2_cur.next.val + carry
        if ans_cur.next.val >= 10:
            ans_cur.next.val = ans_cur.next.val % 10
            carry = 1
        else:
            carry = 0
        # Move to next node
        ans_cur = ans_cur.next
        l1_cur = l1_cur.next
        l2_cur = l2_cur.next
        # If the last node will carry, linked_list needs to append one more node.
        if i == ans_len-2 and carry == 1:
            ans_cur.next = ListNode(1, None)
    #######################
    return ans


def count_linked_list_len(linked_list):
    length = 0
    cur = linked_list
    while cur is not None:
        length += 1
        cur = cur.next
    return length

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
