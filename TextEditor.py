class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class TextEditor:
    def __init__(self):
        self.cursor = None
        self.head = None

    def insert(self, text):
        new_node = Node(text)
        if not self.head:
            self.head = new_node
            self.cursor = self.head
        else:
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            if self.cursor.next:
                self.cursor.next.prev = new_node
            self.cursor.next = new_node
            self.cursor = new_node

    def delete(self):
        if self.cursor.prev:
            self.cursor.prev.next = self.cursor.next
            if self.cursor.next:
                self.cursor.next.prev = self.cursor.prev
            self.cursor = self.cursor.prev
        elif self.cursor.next:
            self.head = self.cursor.next
            self.head.prev = None
            self.cursor = self.head

    def move_cursor_left(self):
        if self.cursor.prev:
            self.cursor = self.cursor.prev

    def move_cursor_right(self):
        if self.cursor.next:
            self.cursor = self.cursor.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end='')
            current = current.next
        print()

if __name__ == "__main__":
    text_editor = TextEditor()

    while True:
        print("Options:")
        print("1. Insert text")
        print("2. Delete character")
        print("3. Move cursor left")
        print("4. Move cursor right")
        print("5. Display text")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to insert: ")
            text_editor.insert(text)
        elif choice == "2":
            text_editor.delete()
        elif choice == "3":
            text_editor.move_cursor_left()
        elif choice == "4":
            text_editor.move_cursor_right()
        elif choice == "5":
            text_editor.display()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
