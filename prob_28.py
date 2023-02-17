import numpy as np

SIZE = 1001

top_right_diag = 0
top_left_diag = 0
bot_left_diag = 0
bot_right_diag = 0

# Top Right Diagonal sum
for i in range(3, SIZE + 1, 2):
    square = i**2
    top_right_diag += square
    top_left_diag += square - i + 1
    bot_left_diag += square - 2 * i + 2
    bot_right_diag += square - 3 * i + 3

print(top_right_diag + top_left_diag + bot_left_diag + bot_right_diag + 1)
