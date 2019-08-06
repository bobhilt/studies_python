# Your mission is to write a program that can display a line of text in ASCII art in a style you are given as input.

#  	Game Input
# Input
# Line 1: the width L of a letter represented in ASCII art. All letters are the same width.

# Line 2: the height H of a letter represented in ASCII art. All letters are the same height.

# Line 3: The line of text T, composed of N ASCII characters.

# Following lines: the string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Represented in ASCII art.

# Output
# The text T in ASCII art.
# The characters a to z are shown in ASCII art by their equivalent in upper case.
# The characters that are not in the intervals [a-z] or [A-Z] will be shown as a question mark in ASCII art.
# Constraints
# 0 < L < 30
# 0 < H < 30
# 0 < N < 200
# Example 1
# Input
# 4
# 5 
# E
#  #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### 
# # # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # 
# ### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## 
# # # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       
# # # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  
# Output
# ### 
# #   
# ##  
# #   
# ### 
# Example 2
# Input
# 4
# 5
# MANHATTAN
#  #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### 
# # # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # 
# ### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## 
# # # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       
# # # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  
# Output
# # #  #  ### # #  #  ### ###  #  ###  
# ### # # # # # # # #  #   #  # # # #  
# ### ### # # ### ###  #   #  ### # #  
# # # # # # # # # # #  #   #  # # # #  
# # # # # # # # # # #  #   #  # # # # 
# ------------------------------------
import sys, re
def clean_data(s):
    s=s.upper()
    return re.sub('[^A-Z]+', '?', s.upper())

def get_row(i,t,letters):
    s = ''
    for c in t:
        s+= letters[i][c]
    return s

w = int(input())
h = int(input())
t = input()
letters = [dict() for x in range(h)]

# get ascii art definition
for i in range(h):
    row = input()
    for k,v in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ?'):
        letters[i][v]= row[k*w:(k+1)*w]
    # print(letters[i], file=sys.stderr)

cleaned_text = clean_data(t)
for i in range(h):
    print( get_row(i, cleaned_text, letters))

