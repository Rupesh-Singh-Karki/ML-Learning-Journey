#1
import matplotlib.pyplot as plt
import numpy as np
# That line is only for jupyter notebooks, if you are using another editor,
#  you'll use: "plt.show()" at the end of all your plotting commands to have the figure pop
# up in another window. For jupyter notebook use "%matplotlib inline"


x = np.linspace(0, 5, 11)
y = x ** 2

plt.plot(x, y, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')


plt.subplot(1,2,1)
# This function creates a grid of subplots. In this case:

# The 1 means one row.
# The 2 means two columns.
# The 1 refers to the first subplot (positioned at the left)
plt.plot(x, y, 'r--') # More on color options later
plt.subplot(1,2,2)
# This activates the second subplot in the grid (positioned to the right)
plt.plot(y, x, 'g*-')

plt.show()