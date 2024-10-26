class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        return self.sorted_merge(left, right)

    def sort(self):
        self.head = self.merge_sort(self.head)

    def merge_two_sorted_lists(self, other):
        merged_list = LinkedList()
        merged_list.head = self.sorted_merge(self.head, other.head)
        return merged_list


# Приклад використання
llist1 = LinkedList()
llist1.insert_at_end(15)
llist1.insert_at_end(10)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(20)
llist2.insert_at_end(3)
llist2.insert_at_end(2)

print("Перший список:")
llist1.print_list()

print("Другий список:")
llist2.print_list()

print("Реверсований перший список:")
llist1.reverse()
llist1.print_list()

print("Відсортований перший список:")
llist1.sort()
llist1.print_list()

print("Об'єднання відсортованих списків:")
merged_list = llist1.merge_two_sorted_lists(llist2)
merged_list.print_list()
