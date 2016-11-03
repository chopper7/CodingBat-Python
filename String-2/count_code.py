# Coding Bat / Python / String-2 / "count_code"
# URL -- http://codingbat.com/prob/p186048

"""
Return the number of times that the string 'code' appears anywhere in
the given string, except we'll accept any letter for the 'd', so 'cope'
and 'cooe' count too.
count_code('aaacodebbb') → 1
count_code('coAcodeBcoleccoreDD') → 3
count_code('cozexxcope') → 2
"""

def count_code(str):
  codecount = 0
  slices = [str[i-1:i+3] for i in range(1, len(str)-1)]
  for s in slices:
    if len(s) < 4:
      break
    else:
      if s[:2] == 'co' and s[3] == 'e':
        codecount +=1
  return codecount