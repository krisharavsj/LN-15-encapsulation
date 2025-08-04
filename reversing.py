class StringReverser:
    def __init__(self, text):
        self.text = text
    def reverse_letters(self):
        return self.text[::-1]
user_input = input("Enter a string: ")
reverser = StringReverser(user_input)
print("Reversed string letter by letter:", reverser.reverse_letters())
