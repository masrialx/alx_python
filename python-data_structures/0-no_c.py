#!/usr/bin/python3
no_c = __import__('0-no_c').no_c

word = "School"
new_word = no_c(word)

print(new_word)
print(word)

# Update the original 'word' variable with the new_word
word = new_word

print(word)
