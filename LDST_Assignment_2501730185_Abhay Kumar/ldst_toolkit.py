# Name: Abhay Kumar
# Roll No.: 2501730185
# Section: A

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = x
        self.size += 1

    def resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        new_arr = [None] * (self.capacity * 2)
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity *= 2

    def pop(self):
        if self.size == 0:
            return "Underflow"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def __str__(self):
        return str(self.arr[:self.size])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_at_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete_by_value(self, x):
        temp = self.head
        prev = None
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
        print("Value not found")

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new = Node(x)
                new.next = temp.next
                new.prev = temp
                if temp.next:
                    temp.next.prev = new
                temp.next = new
                return
            temp = temp.next

    def delete_at_position(self, pos):
        temp = self.head
        if pos == 0:
            if self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            return
        for _ in range(pos):
            if not temp:
                return
            temp = temp.next
        if not temp:
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return "Underflow"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.data if self.head else None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            return "Underflow"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        return self.head.data if self.head else None


def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in expr:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.pop() != pairs[ch]:
                return False
    return stack.head is None


# Main Testing
if __name__ == "__main__":
    print("--- Dynamic Array ---")
    da = DynamicArray(2)
    for i in range(10):
        da.append(i)
        print(da)
    print("Pop:", da.pop(), da.pop(), da.pop())
    print(da)

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(1)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(3)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.insert_at_end(6)
    sll.traverse()
    sll.delete_by_value(4)
    sll.traverse()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    for i in range(1, 6):
        dll.insert_at_end(i)
    dll.traverse()
    dll.insert_after(3, 99)
    dll.traverse()
    dll.delete_at_position(1)
    dll.traverse()

    print("\n--- Stack ---")
    st = Stack()
    st.push(10)
    st.push(20)
    print(st.peek())
    print(st.pop())

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.front())
    print(q.dequeue())

    print("\n--- Parentheses Checker ---")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "→", is_balanced(t))

