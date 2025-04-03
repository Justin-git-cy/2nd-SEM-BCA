def word_count(text):
    words = text.split()  # Splitting text by spaces
    return len(words)

text = input("Enter a sentence or paragraph: ")
print("Word count:", word_count(text))
