#! /usr/bin/env python3

# You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

# Return the minimum number of different frogs to finish all the croaks in the given string.

# A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

# Example 1:

# Input: croakOfFrogs = "croakcroak"
# Output: 1 
# Explanation: One frog yelling "croak" twice.
# Example 2:

# Input: croakOfFrogs = "crcoakroak"
# Output: 2 
# Explanation: The minimum number of frogs is two. 
# The first frog could yell "crcoakroak".
# The second frog could yell later "crcoakroak".
# Example 3:

# Input: croakOfFrogs = "croakcrook"
# Output: -1
# Explanation: The given string is an invalid combination of "croak" from different frogs.

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    word = "croak"
    running_count = 0
    frogs = []
    result = 0
    for letter in croakOfFrogs:
        if letter == "c":
            running_count += 1
            frogs.append(1)
        else:
            has_found_match = False
            for index in range(0, len(frogs)):
                if frogs[index] == word.index(letter):
                    has_found_match = True
                    frogs[index] += 1
                    if letter == 'k':
                        result = max(running_count, result)
                        frogs.pop(index)
                        running_count -= 1
                    break
            if not has_found_match:
                return -1

    return result

print(minNumberOfFrogs("croak"))
print(minNumberOfFrogs("croakcroak"))
print(minNumberOfFrogs("crocarkoak"))
print(minNumberOfFrogs("ccrocarkoakroa"))
print(minNumberOfFrogs("crocarkoakcroak"))
