text = input("Enter text: ")

characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("?") + text.count("!")

print("Characters:", characters)
print("Words:", words)
print("Sentences:", sentences)