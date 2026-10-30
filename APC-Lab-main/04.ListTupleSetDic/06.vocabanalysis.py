book1 = input("Enter text of Book 1: ")
book2 = input("Enter text of Book 2: ")

words1 = set(book1.lower().split())
words2 = set(book2.lower().split())

# Unique words in each book
print("Unique words in Book 1:")
print(words1)

print("Unique words in Book 2:")
print(words2)

# Common words
common = words1.intersection(words2)
print("Common words:")
print(common)

# Words unique to each book
only_book1 = words1.difference(words2)
only_book2 = words2.difference(words1)

print("Words unique to Book 1:")
print(only_book1)

print("Words unique to Book 2:")
print(only_book2)

# Total unique words
all_words = words1.union(words2)

print("Total unique words across both books:", len(all_words))
