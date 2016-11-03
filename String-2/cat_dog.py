# Coding Bat / Python / String-2 / "cat_dog "
# URL -- http://codingbat.com/prob/p164876

# 
"""
Return True if the string "cat" and "dog" appear the same number of
times in the given string.
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

#helper function
def countpets(full_string, find_string):
    count = 0
    for i in range(len(full_string)-1):
      if full_string[i:(i+3)] == find_string:
          count += 1
    return count

def cat_dog(str):  
  # count "cat", count "dog", then compare counts
  return countpets(str, 'cat') == countpets(str, 'dog')