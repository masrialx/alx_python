#!/usr/bin/env python3
def multiple_returns(sentence):
    if not sentence:
        return 0, None
    else:
        return len(sentence), sentence[0]

# Test case
sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
